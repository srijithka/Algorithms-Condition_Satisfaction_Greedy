def recursive_call(mp, j, lead_to_list_sizes, leads, var_list):
    pos_lhs = 1
    if(var_list[leads[j][-1]] == 1):
      return
    for k in range(lead_to_list_sizes[j]):
      pos_lhs = pos_lhs and var_list[leads[j][k]]
      if(pos_lhs == 0):
        break
    res = 0
    if(pos_lhs == 1):
      if(var_list[leads[j][-1]] == 1):
        res = 1
      var_list[leads[j][-1]] = 1
    else:
      return

    if leads[j][-1] not in mp or res == 1:
      return

    for k in mp[leads[j][-1]]:
      if(var_list[leads[k][-1]] == 1):
        continue
      recursive_call(mp, k, lead_to_list_sizes, leads, var_list)
      



def calc(n, lead_size, false_size, lead_to_list_sizes, false_must_exist_sizes, leads, falses):
  var_list = [0] * n
  mp = {}
  for i in range(lead_size):
    lhs = 1
    for j in range(lead_to_list_sizes[i]):
      lhs = lhs and var_list[leads[i][j]]
      if leads[i][j] in mp:
        mp[leads[i][j]].append(i)
      else:
        mp[leads[i][j]] = [i]
      
    res = 0
    if(lhs == 1):
      if(var_list[leads[i][-1]] == 1):
        res = 1
      var_list[leads[i][-1]] = 1
    else:
      continue

    if leads[i][-1] not in mp or res == 1:
      continue
    for j in mp[leads[i][-1]]:
      if(var_list[leads[j][-1]] == 1):
        continue
      recursive_call(mp, j, lead_to_list_sizes, leads, var_list)

  flag = True
  for i in range(false_size):
    fl = 0
    for j in range(false_must_exist_sizes[i]):
      if(var_list[falses[i][j]] == 0):
        fl = 1
        break
    if(fl == 0):
      flag = False
      break
  if(flag == False):
    return []
  return var_list
      


import pickle
file_path = 'test_set_small_instances (1)'
examples_of_instances = pickle.load(open(file_path, 'rb'))

k_list =[]

last_points_list = []

OPT_list = []

test = examples_of_instances['numInstances']

solu_list = []

for i in range(test):
   n = examples_of_instances['n_list'][i]
   lead_to_size = examples_of_instances['P_list'][i]
   false_must_exist = examples_of_instances['Q_list'][i]
   lead_to_list_sizes = examples_of_instances['k_list'][i]
   false_must_exist_sizes = examples_of_instances['m_list'][i]
   T_List = examples_of_instances['T_list'][i]
   M_List = examples_of_instances['M_list'][i]
   solution = calc(n, lead_to_size, false_must_exist, lead_to_list_sizes, false_must_exist_sizes, T_List, M_List)
   solu_list.append(solution)
   print("next")


file_path = 'small_solutions' 
# Open the file in binary write mode ("wb") and dump the dictionary into it
with open(file_path, 'wb') as file:
    pickle.dump(solu_list, file)



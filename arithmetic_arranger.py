SPACES_SIZE = 4

def arithmetic_arranger(problems,resolve=False):
  
  arranged_problems=[]
  
  if len(problems)<=5:
    for problem in problems:

      problem_items = problem.split(" ",3)

      if not (problem_items[1]=="+") and not (problem_items[1]=="-"):
        return "Error: Operator must be '+' or '-'."

      if not problem_items[0].isdigit() or not problem_items[2].isdigit():
        return "Error: Numbers must only contain digits."

      if len(problem_items[0])>4 or len(problem_items[2])>4:
        return "Error: Numbers cannot be more than four digits."
     
    
      if len(problem_items)==3:
        if resolve:
          problem_items.append(resolveProblem(problem_items))

        arranged_problems.append(problem_items)

      else:
        return "Error: Invalid operation."

  else:
    return "Error: Too many problems."

  return arranged_problems_to_str(arranged_problems)

def resolveProblem(problem):
  
  if problem[1]=='+':
    return str(int(str(problem[0])) + int(str(problem[2])))
  
  return str(int(str(problem[0])) - int(str(problem[2])))

#convert the arranged_problems output in string and format it
def arranged_problems_to_str(arranged_problems):

  lines = ["","","",""]
  arranged_problems_str =""

  for i,problem in enumerate(arranged_problems):

    lmax = getMaxLen(problem)
    operands = [int(problem[0]),int(problem[2])]

    lines[0]+= getSpaces(lmax,problem[0]) + problem[0] + distance(i,len(arranged_problems))
    
    aux = problem[1] + " "*(len(str(max(operands))) + 2 -(len(problem[1])+len(problem[2]))) + problem[2]
    
    lines[1]+= getSpaces(lmax,aux)+ aux + distance(i,len(arranged_problems))
    
    mSeparator = buildSeparator(lmax, len(aux))

    lines[2]+= getSpaces(lmax,mSeparator) + mSeparator + distance(i,len(arranged_problems))
    
    if len(problem)==4:
      lines[3]+= getSpaces(lmax,problem[3]) + problem[3] + distance(i,len(arranged_problems))

  lines[0]+="\n"
  lines[1]+="\n"

  if len(problem)==4:
    lines[2]+="\n"

  for line in lines:
    arranged_problems_str+=line
  
  return arranged_problems_str

#calculate the spaces needed to complete a line relative to the longest line length
#add the longest line length, plus two spaces: one for the operator, one for the space between the operator and the operand, and subtract the length from the current string
def getSpaces(lmax,s):
  return " "*(lmax + 2 - len(s))

#generate a separator with '-' ,relative to the longest line
def buildSeparator(lmax,s):
  return "-"*(lmax + (abs(lmax-s)))

#gets the length of the longest line in a problem 
#if the problem contains a solution, returns the maximum length between the solution value and the operands
def getMaxLen(problem):

  operands = [int(problem[0]),int(problem[2])]

  if len(problem)==3:
    return len(str(max(operands)))

  if problem[1]=="+":
    return len(problem[3])
    
  return len(str(max(int(problem[3]), max(operands))))

#generate a distance of spaces , if is the last item return ""
def distance(i,size):
  if i == size-1:
    return ""

  return SPACES_SIZE*" "
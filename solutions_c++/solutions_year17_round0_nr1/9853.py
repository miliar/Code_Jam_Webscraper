#include <iostream>



unsigned int inverse(unsigned int panecakes, int position, unsigned int mask){
  unsigned int y = 0;
  
  mask <<= position;

  y = panecakes & mask;

  y = ~y & mask;
  panecakes = panecakes & (~mask);
  panecakes = panecakes | y;
  return panecakes;
  
}

/***
 *returns -1 if IMPOSSIBLE
 *returns positive integer if can do it
 */
int solver(char* s, int k){
  char* tmp = s;
  int result = 0, combo = 0, position = 0, i = 0, inv = 0;
  unsigned int panecakes = 0, inversions = 0, counter = 0, mask = 0;
  //----------creating mask---------
  for(i = 0; i < k; i++){
    mask <<= 1;
    mask |= 1; 
  }

  //----------before flips----------
  while(*(tmp)){
    counter++;
    panecakes <<= 1;
    if(*(tmp++) == '+'){
      panecakes |=1;   
      combo = 0;
    }
    else{
      inversions++;
      if(!combo){
	combo = 1;
	position = counter - 1;
      }
      else{
	if(++combo == k){
	  panecakes = inverse(panecakes, position, mask);
	  result++;
	  combo = 0;
	  inversions -= k;
	}
	}

    }
  }
  if (inversions == 0)
    return result;
  if(k == counter && inversions != 0 && inversions < counter)
    return -1;

  //----------flips-----------------
  
  for(i = 0; i < counter - k; i++){
    if(!((panecakes >> i) & 1)){
      panecakes = inverse(panecakes, i, mask);
      result++;
    }
  }
  for(; i < counter; i++){
    if(!((panecakes >> i) & 1))
      inv++;
      }
  if(inv == k)
    return ++result;
  if(inv==0)
    return result;

  //----------after flips-----------
  return  -1;

}


int main(){

  
  int cases_number = 0, k = 0, i = 0;
  char* s = new char[10];
  std::cin >> cases_number;

  for(; i < cases_number; i ++){ 
   std:: cin >> s >> k;
   int res = solver(s,k);
   if(res == -1)
     std::cout << "Case #"<< i+1 << ": " << "IMPOSSIBLE" << std::endl;
   else
     std::cout << "Case #"<< i+1 << ": " << res << std::endl;
  }
  delete s;
}


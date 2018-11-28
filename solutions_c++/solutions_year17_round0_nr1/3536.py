#include <cstdio>
#include <cstring>
#include <vector>

void print(std::vector<bool>& arr){
  for(int i = 0; i < arr.size(); i++){
    printf("%c ", (arr[i]?'1':'0'));
  }
  printf("\n");
}

void flip(std::vector<bool>& arr, int p, int k){
  //printf("flip %d\n", p);
  for(int i = 0; i < k; i++){
    arr[p+i] = !arr[p+i];
  }
  //print(arr);
}

int solve(std::vector<bool>& arr, int k){
  int flipCount = 0;
  //print(arr);
  for(int i = 0; i <= arr.size()-k; i++){
    if(!arr[i]){
      flip(arr, i, k);
      flipCount++;
    }
  }
  for(int i = arr.size()-k+1; i < arr.size(); i++){
    if(!arr[i])
      return -1;
  }
  return flipCount;
}

int getMinFlip(char s[2000], int k){
  int n = strlen(s);
  //printf("%s %d\n", s, k);
  std::vector<bool> arr;
  arr.resize(n);
  for(int i = 0; i < n; i++)
    arr[i] = (s[i]=='+')?true:false;
  return solve(arr, k);
}

int main(){
  int T, K;
  char s[2000];
  scanf("%d\n", &T);
  int t = 1;
  while(t < T+1){
    scanf("%s %d\n", s, &K);
      int ans = getMinFlip(s, K);
      if(ans >= 0)
        printf("CASE #%d: %d\n", t, ans);
      else
        printf("CASE #%d: IMPOSSIBLE\n", t);
    t++;
  }
}

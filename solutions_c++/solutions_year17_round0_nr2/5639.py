#include <cstdio>
#include <cstring>

int verify(unsigned long long num){
  unsigned long long newnum = num / 10;
  if(newnum == 0) return true;

  if(newnum % 10 > num % 10){
    return false;

  }

  return verify(newnum);

}

unsigned long long getValue(unsigned long long num, unsigned long long base){
  // 32400
  //   400
  //   100
  return (num / base) % 10;

}

unsigned long long find(unsigned long long num, unsigned long long base){
  //printf("try %lld %lld\n",num,base);
  if(verify(num)) return num;

  if(num == 1) return 1;

  if(getValue(num, base) == 0) return find(num - base, base * 10);
  return find(num - base, base);

}

int main(){
  freopen("B-large.in","r",stdin);
  int N;
  scanf("%d",&N);
  for(int i=1;i<=N;i++){
    unsigned long long a;
    scanf("%llu",&a);
    printf("Case #%d: %llu\n", i, find(a, 1));
  }
  return 0;
}

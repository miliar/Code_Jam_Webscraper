#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdio>
#define ll long long int
#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)
#define modulo(S, N) ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))
ll num_bits(ll k){
  ll b=0;
  while(k>0){
    k=k/2;
    b++;
  }
  return b;
}
using namespace std;
int main(){
  int T;
  cin>>T;
  for(int t_i=0;t_i<T;t_i++){
    long long int n;
    long long int k;
    scanf("%lld %lld",&n,&k);
    long long int d=num_bits(k);
    ll x=(1<<(d-1))-1;
    ll t=k-x;
    ll unit=n;
    ll z=n-x;
    for(int i=0;i<d-1;i++){
      unit=(unit-1)/2;
    }
    ll a,b;
    b=n-x-(x+1)*unit;
    a=x+1-b;
    //cout<<unit<<" "<<t<<" "<<b<<" "<<a<<endl;
    if(t>b){
      printf("Case #%d: %lld %lld\n",t_i+1,(unit)/2,(unit-1)/2);
    }
    else{
      unit++;
      printf("Case #%d: %lld %lld\n",t_i+1,(unit)/2,(unit-1)/2);
    }
  }
  return 0;
}

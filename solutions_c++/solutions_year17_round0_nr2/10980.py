#include <bits/stdc++.h>

using namespace std;
uint64_t numdigits(uint64_t n){
  uint64_t c=0;
  while(n)n/=10,c++;
  return c;
}

int iscorrect(uint64_t n){
  string s=to_string(n);
  for(int i=0;i<s.size();i++){
    if(s[i]<s[i-1])
    return 0;
  }
  return 1;
} 
int main(){
  FILE *fin = freopen("B-small-attempt0.in","r",stdin);
	FILE *fout = freopen("out.txt","w",stdout);
  uint64_t T,N;
  cin>>T;
  long long i=1;
  while(T--){
    cin>>N;
    uint64_t num=numdigits(N);
    uint64_t c=1;
    uint64_t k=N;
    while(num--){
        //cout<<num<<" "<<k<<" ";
      if(iscorrect(k)){
        cout<<"Case #"<<i<<": "<<k<<"\n";
        c=0;
        break;
      }
      //cout<<" "<<1<<" ";
      string str=to_string(k);
      str[num]='9';
      if(num-1>=0 && str[num-1]!='0')str[num-1]-=1;
      if(str.size()>9){
          string s1=str.substr(0,9);
          string s2=str.substr(9,str.size()-9);
          k=stoi(s1)*pow(10,str.size()-9)+stoi(s2);
          //cout<<" "<<k;
      }
      else k=stoi(str);
      //cout<<k<<"\n";
    }
    if(c){
      k=pow(10,num)-1;
      cout<<"Case #"<<i<<": "<<k<<"\n";
    }
    i++;
  }
  return 0;
}

#include <bits/stdc++.h>
#define op(a) "Case #"<<a<<": "
#define ll long long
using namespace std;
 int cn[2]={0};
//ll fn1(string s,int l);
/*ll fn2(string s,int l){
   //if(cn[1]==0) return 0;
  //if((cn[1]%l!=0&&cn[0]==0)||cn[1]<l) return -1;
  int  i=s.length()-1,ans=0;
  cout<<s<<"==123";
  while(i>=0){
    if(s[i]=='-'){
    for(int j=0;j<l;j++){
       if(i-j<0) return -1;
       s[i-j]=(s[i-j]=='+'?'-':'+');   
    }
    i--;
    cout<<s<<"  =xcv"<<ans<<endl;
    ans++;
    }
  }
         return ans;
}*/

ll fn1(string s,int l){
int  n=s.length();
  for(int i=0;i<n;i++){
     if(s[i]=='+')
          cn[0]++;
        else cn[1]++;
  }
  if(cn[1]==0) return 0;
  if((cn[1]%l!=0&&cn[0]==0)||cn[1]<l) return -1;
  int i=0,ans=0,ans1=0;
  string ss=s;
  while(i<n){
    if(s[i]=='-'){
    for(int j=0;j<l;j++){
      if(i+j>=n) return -1;
       s[i+j]=(s[i+j]=='+'?'-':'+');
    }
  //  cout<<s<<" =assd\n";
    ans++;
    }
    i++;
  }
     return ans;//min(ans,ans1);
}
int main(int argc, char const *argv[])
{
	ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
     int No_testCase; fin>>No_testCase;
  
    for(int test_id=1;test_id<=No_testCase;test_id++){    
       string s;int l; 
       fin>>s>>l;
       int x=fn1(s,l);
       if(x!=-1)
       fout<<"Case #"<<test_id<<": "<<(x)<<endl;
     else{
      fout<<op(test_id)<<"IMPOSSIBLE"<<endl;
     }
   }
	return 0;
}
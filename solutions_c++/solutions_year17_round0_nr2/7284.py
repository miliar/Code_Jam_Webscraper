#include<bits/stdc++.h>
#define ll long long int

using namespace std;

template <typename T>
string NumberToString ( T Number ){
	stringstream ss;
	ss << Number;
	return ss.str();
}


bool ispossible(ll n){
   string s=NumberToString(n);
   int sz=s.size();
   if(sz==1) return true;
   for(int i=1;i<sz;i++){
     if(s[i]<s[i-1]) return false;
   }
   return true;
}

bool case1(string s){
   char c=s[0];
   for(int i=1;i<s.size();i++){
    if(s[i]!=c && i!=s.size()-1) return false;
   }
   return true;
}

int main(){
freopen("BB.in","r",stdin);
freopen("out_codejam1.txt","w",stdout);
int t;
cin>>t;
for(int tc=1;tc<=t;tc++){
   ll n;
   cin>>n;
   cout<<"Case #"<<tc<<": ";
   if(ispossible(n)) {
      cout<<n<<endl;
   }
   else {
    string s=NumberToString(n);
    string ans="";
    if(case1(s)){
       int temp=(s[0]-'0')-1;
       if(temp) ans=(char)(temp+'0');
       for(int i=0;i<s.size()-1;i++) ans=ans+'9';
    }
    else {
        int idx=s.size()+1;
        for(int i=0;i<s.size()-1;i++){
            if(s[i]>s[i+1]){
                idx=i+1;
                if(s[i]==s[i-1]) idx=i;
                int temp=(s[idx-1]-'0')-1;
                s[idx-1]=(char)(temp+'0');
                break;
            }
        }
        for(int i=0;i<idx;i++) ans=ans+s[i];
        for(int i=idx;i<s.size();i++) ans=ans+'9';
    }
    int j=0;
    while(ans[j]=='0') j++;
    for(int i=j;i<s.size();i++) cout<<ans[i];
    cout<<endl;
   }
}
return 0;
}

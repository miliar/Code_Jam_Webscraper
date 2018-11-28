#include<bits/stdc++.h>
#define sc(a) scanf("%lld\n",&a)
#define sf(a) scanf("%lf",&a)
using namespace std;
int main() {
//freopen("naya.in","r",stdin);
//freopen("output.txt","w",stdout);

    long long n,t;long long nmb,rnm;
    sc(t);
    string s;
    int c=1,br=1,len;int cc=0;
    int a=1;
   while(t--)
       {
       int ind;
       br=1;
      //sc(n);
       //s=std::to_string(n);
       cin>>s;
          len=s.length();ind=len-1;
       for(int i=0;i<len-1;i++)
           {
           if(s[i]>s[i+1])
               {br=0;ind=i+1;break;}
       }
       if(br==1){
            cout<<"Case #"<<a++<<": ";
for(int i=0;i<len;i++)
           cout<<s[i];
           cout<<endl;
       continue;
       }
       int i=len-1;
      // cout<<"ind "<<ind<<endl;
       for(int i=ind;i<len;i++)
           s[i]='9';
       s[ind-1]=s[ind-1]-1;
     /*  for(i=len-1;i>0;i--)
           {
           if(s[i]<=s[i-1])
            s[i]='9';
           else break;
       }*/
            cout<<"Case #"<<a++<<": ";
       for(int i=0;i<len;i++)
           if(s[i]!='0')
           cout<<s[i];
           cout<<endl;
   }
}


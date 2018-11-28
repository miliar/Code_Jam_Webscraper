#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define f(i,st,en)for(int i=st;i<en;i++)
#define fi(i,st,en)for(int i=st;i<=en;i++)
typedef vector<int>vi;
typedef long long int ll;

int conv(string str)
{
  stringstream ss(str);
  int i;
  ss >> i;
  return i;
}

string con(int a){
     stringstream ss;
     ss << a;
     string str = ss.str();
     return str;
}

bool fun(string str){

      if(str.length()==1)
         return true;

      for(int i=0;i+1<str.size();i++){
           if((str[i]-'0')>(str[i+1]-'0'))
                return false;
      }
      return true;
}
string rec(string str){

      int p=-1;
       for(int i=0;i+1<str.length();i++){
             if((str[i]-'0')>(str[i+1]-'0')){
                    p=i;
                    break;
             }
       }
       if(p==-1)
         return str;
       else
       {
           string pre,post;
           for(int i=0;i<=p;i++)pre+=str[i];
         //cout<<pre<<endl;
          if(pre[pre.length()-1]!='1'){
            pre[pre.length()-1]=((pre[pre.length()-1]-'0')-1)+'0';
            }
            else
               {

                   if(pre.length()==1&&pre[0]=='1'){
                       pre="0";
                   }
                   else{
                        int len=pre.length();
                        pre="";
                        for(int i=0;i<len-1;i++)
                             pre+="9";
                      }
               }
          //cout<<pre<<endl;
               pre=rec(pre);

               for(int i=p+1;i<str.length();i++)
                    post+='9';
            return pre+post;
       }
}
int n;
string str;
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("out_large","w",stdout);


    int t;
    scanf("%d",&t);

    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);

      cin>>str;

      /*if(str[0]!='9'){
      for(int i=str.size()-1;(i-1)>=0;i--){
          if(str[i]=='0'&&str[i-1]=='0'){
              str[i]='9';
              continue;
          }
          if(str[i-1]=='0')
             {
                str[i]='9';
                continue;
             }
          if((str[i]-'0')<(str[i-1]-'0')){
                str[i]='9';
                str[i-1]=((str[i-1]-'0')-1)+'0';
          }
      }

      for(int i=0;i<str.size();i++)
         {
            if(i==0&&str[i]=='0')
               continue;
            else
               cout<<str[i];
         }
       cout<<endl;
       }
       else{
             cout<<"8";
             for(int i=1;i<str.length();i++)
                 cout<<"9";
             cout<<endl;
       }*/
       string output=rec(str);
       bool flag=false;
       for(int i=0;i<output.size();i++){
             if(output[i]!='0')flag=true;

             if(flag)
               cout<<output[i];
       }
       cout<<endl;
    }
    return 0;
}

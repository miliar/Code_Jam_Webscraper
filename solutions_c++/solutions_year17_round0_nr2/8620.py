#include<bits/stdc++.h>
using namespace std;
string s;
int main(){
freopen("input_file_name.in","r",stdin);
freopen("output_file_name.out","w",stdout);
  long long int i;

 int k=0;
  int t;
  int j2=0;
  cin >> t;
  while(t--){

  cin >> s;
        int temp=0,temp2;
        for(int i=0;i<s.size()-1;i++)
        {   if(j2)
                {
                    s[i]='9';
                }
            else
          {
             if(s[i]>s[i+1])
              {
                temp=i;
                temp2=s[i];
                s[i]=s[i]-1;
                j2=1;
              }
          }
        }

        int fk=0;
        if(j2)
            s[s.size()-1]='9';
        if(temp!=0)
            s[temp] = '9';
       for(int i=temp-1;i>=0;i--)
        {
             if(s[i]==temp2)
                s[i]=(i!=0?'9':s[i]-1);
             else
             {
                 s[i+1]=temp2-1;
                 break;
             }
        }



    j2=0;
     for(int i=0;i<s.size();i++)
     {
            if(s[i]=='0')
            {
                s=s.substr(1,s.size()-1);
            }
     }
     cout<<"Case #"<<++k<<": "<<s<<endl;
      temp=0;
   }
return 0;

}

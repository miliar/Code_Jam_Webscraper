#include<bits/stdc++.h>



using namespace std;

int cnt =0;
string str;


string get(string str)
{
    if(str.length()==1)
        return str;
    int maxi = str[0]-'0';
    for(int i=1;i<str.length();i++)
    {
        maxi =max(maxi,str[i]-'0');
        if(str[i]>=str[i-1])
        continue;
        else
        {
           if(maxi<=1)
           {
               string temp ;
               for(int i=0;i<str.length()-1;i++)
                temp.push_back('9');
               return temp;
           }
           else
           {
               for(int j=i;j<str.length();j++)
                str[j]='9';
                str[i-1]=str[i-1]-1;

               for(int j=i-2;j>=0;j--)
               {
                  if(str[j]>str[j+1])
                  {


                    str[j]=str[j]-1;
                    for(int k=j+1;k<str.length();k++)
                        str[k]='9';
                  }

               }
               if(str[0]=='0')
               {
                reverse(str.begin(),str.end());
                str.pop_back();
                reverse(str.begin(),str.end());


               }

           }



        }
    }
    return str;
}
int main()
{
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

    int d =0;

    int k,t;
    cin>>t;
    while(t--)
    {
        ++cnt;
        cin>>str;
        string ans = get(str);


        cout<<"Case #"<<cnt<<": "<<ans<<"\n";




    }
}


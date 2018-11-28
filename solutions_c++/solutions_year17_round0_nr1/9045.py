 #include<bits/stdc++.h>

 using namespace std;

 int ct;

int modify(string s,int k)
{
  int i,j,sgn=0,l=s.size();

  for(i=0;i<s.size();i++)
    {
       if(s[i]=='-')
        {
          if((l-i)>=k)
           {
               sgn=1;
                 ct++;

              for(j=i;j<i+k;j++)
               {
                if(s[j]=='-')
                   s[j]='+';
                else s[j]='-';
               }
           }
         else
           return -1;
        }
    }

  if(!sgn)

      return ct;

  else return (modify(s,k));
}


int main()
{
  freopen("A-large.in","r",stdin);
  freopen("rakesh1.txt","w",stdout);

 int k,t,i,j,m;

  cin>>t;

 for(k=1;k<=t;k++)
  {
    string s;

     cin>>s>>m;

    ct=0;

   int ans =modify(s,m);

   cout<<"case #"<<k<<":"<<" ";

if(ans==-1)

   cout<<"IMPOSSIBLE"<<"\n";

 else

    cout<<ct<<"\n";

 }

return 0;
}

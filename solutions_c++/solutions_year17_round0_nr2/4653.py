#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
int nt=1;
while(t--)	
{
 int i,j,num;
 string s;
cin>>s;

 if( s.size() == 1)
 { cout<<"Case #"<<nt<<": "<<s<<endl; nt++;}
 else
 {
  vector<int>v;
  int k=1;
  for(i=0;i<s.size()-1;i++)
  	 {
         if( ( s[i]-'0' ) <= ( s[i+1] -'0' ) )
         	   v.push_back( s[i]-'0');   
         else
            {
              int u= s[i]-'0' ;
                 u--;
                 v.push_back(u);
                 for(j=i+1;j<s.size();j++)
                 	 v.push_back(9);
                 k=0;
                 break;	
            }	
  	 }
     if(k==1)
      v.push_back(s[ s.size()-1] -'0') ;
      if(v[0] == 0)
        v.erase(v.begin() + 0);
      
      for(i=v.size()-1;i>=1;i--)
          {
            if(v[i] >= v[i-1])
                 continue;
            else
                {
                  v[i]=9;
                  v[i-1]=v[i-1]-1;
                }
          }
      cout<<"Case #"<<nt<<": ";
      if(v[0]!=0)
          cout<<v[0];
     for(i=1;i<v.size();i++)
         cout<<v[i];
     cout<<endl;
     nt++;
 }
}
	return 0;
}
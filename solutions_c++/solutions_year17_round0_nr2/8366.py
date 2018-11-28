
#include <bits/stdc++.h>
using namespace std;

int main()
{
 //freopen("in.txt","r",stdin);
 //freopen("out.txt","w",stdout);


	 int t;
	 int ind;
	 int n;
	 string s;
	 cin>>t;
	 for(int i=1;i<t+1;i++)
	 { cin>>s;
	   if (s.size()==1) {cout<<"Case #"<<i<<": "<<s<<endl;}
	   else {
	  for (int i=0;i<s.size()-1;i++)
      {  if (s[i]>s[i+1]) {  int h=i;
                             while(h>-1 && s[h]==s[i]  )
                             {


                                 h--;
                             }

                            s[h+1]=s[i]-1;

                            for (int j=h+2;j<s.size();j++)
                                s[j]='9';
                             break;
                             }
      }
      if (s[0]=='0') {  cout<<"Case #"<<i<<": ";
                       for (int p=0;p<s.size()-1;p++) cout<<9; cout<<endl;}
     else  cout<<"Case #"<<i<<": "<<s<<endl;}
     }
}




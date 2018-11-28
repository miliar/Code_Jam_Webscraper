#include <bits/stdc++.h>
 using namespace std;

#define ll long long int
#define pb push_back 
#define mp make_pair
#define ff first
#define ss second


int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
   ll n,b,i,j,k,z,x=0,y=0,p,q,l,T,m,ans=0;
    double xx,yy;   
   string s;
   cin>>T;
   for(int t = 1; t <= T; t++)
   {
   	cin>>n;
   	stringstream ss,ss1;
   	ss<<n;

   	s = ss.str();
   	l = s.length();

   	 for( i = 0; i < l-1; i++)
   	 {
   	 	if(s[i] > s[i+1])
   	 	{
   	 		j = i;
   	 		while(j-1 >= 0 && s[j] == s[j-1])
              j--;

            s[j]=s[j]-1;

            for(j = j + 1; j < l ;j++)
            	s[j] = '9';
             
            
            //cout<<s<<endl;
            
             break;
   	 	}
   	 }
   	 ss1<<s;   
     ss1>>ans;
   	 cout<<"Case #"<<t<<": "<<ans<<"\n";
   }



 return 0;
}
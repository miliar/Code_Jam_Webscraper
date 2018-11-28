#include<bits/stdc++.h>

#define vi vector <int>
#define vlli vector <long long>

#define pb push_back
#define mp make_pair

#define ff first
#define ss second

#define foreach(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define all(x) x.begin(),x.end()

#define ll long long

#define INF 3f3f3f3f
#define MOD 1000000007
#define MAXN 1005
using namespace std;

char s[27][28];
int f[27][28];
int R,C;
		
int don()
{
	for(int i=0;i<R;i++)
	 for(int j=0;j<C;j++)
	  if(s[i][j]=='?')
	   return 0;
   return 1;
}
int main()
{
	//N = 1002;
	freopen("A-large.in","r",stdin);
	freopen("out3.txt","w",stdout);
    
	int T;
	scanf("%d",&T);
	int t=1;
	while(T--)
	{
		printf("Case #%d:\n",t++);
		cin >> R >> C ;
        int  all=0;
		for(int i=0;i<R;i++)
		{
			cin >> s[i];
			for(int j=0;j<C;j++)
			 if(s[i][j]=='?')
			  all++;
		}	
		if(all==R*C)
		{
			for(int i=0;i<R;i++)
			{
			 //cin >> s[i];
			 for(int j=0;j<C;j++)
			   cout  << "A";
			  cout << endl;
			}	
		}
		else 
		{
		  int ind;
		  int fg=0;
		  memset(f,0,sizeof(f));
		  
	      for(int i=0;i<R;i++)
		  {
			   for(int j=0;j<C;j++)
			   {
			      //ind++;
			      char ch;
			      if(s[i][j]!='?')
				  {	
					 ch = s[i][j];
					 if(fg==0)
					 {
					 	ind = i;
					 	fg=1;
					 }
					 for(int k=j-1;k>=0;k--)
					  if(s[i][k]!='?')
					   break;
					  else 
					  {
					  	s[i][k]=ch;
					  	
					  }
					 for(int k=j+1;k<C;k++)
					  if(s[i][k]!='?')
					   break;
					  else 
					  {
					  	s[i][k]=ch;
					  }
				  }	
			   }	
	  	  }
	  	  //cout << ind << endl;
		  for(int i=ind-1;i>=0;i--)
		  {
			   for(int j=0;j<C;j++)
			   {
			   	  if(s[i][j]=='?')
			   	   s[i][j]=s[i+1][j];
			   }
		  }
		  for(int i=ind+1;i<R;i++)
		  {
			   for(int j=0;j<C;j++)
			   {
			   	  if(s[i][j]=='?')
			   	   s[i][j]=s[i-1][j];
			   }
		  }
		  for(int i=0;i<R;i++)
			{
			 //cin >> s[i];
			 for(int j=0;j<C;j++)
			   cout << s[i][j] ;
			  cout << endl;
			}	
		}	
		
		//cout << ans << endl;
	}
	
	return 0;
}

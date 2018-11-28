#include <bits/stdc++.h>

#define INF                         (long long)1e15
#define EPS                         1e-9
#define MOD   1000000007
#define checkbit(n,b)                ( (n >> b) & 1)
#define min3(a,b,c)                  ( a<b?(a<c?a:c):(b<c?b:c) )
#define max3(a,b,c)                  ( a>b?(a>c?a:c):(b>c?b:c) )
//dataTypes
#define ll long long int
#define ld long double
#define vi vector<int>
#define vll vector<long long int>
#define vp vector< pair<long long, long long > >
//STLFunctions
#define pb(x) push_back(x)
#define maxElement(v) *max_element(v.begin(), v.end())
#define minElement(v) *min_element(v.begin(), v.end())
#define SORT(v) sort(v.begin(),v.end())
#define mp(x,y) make_pair(x,y)
//loops
#define f(i,a,n) for( i=a; i<n; i++)

using namespace std;

int main() {
   int t, it;
   cin>>t;
   for(it=1; it<=t; it++)
   {
   	cout<<"Case #"<<it<<": "<<endl;

   	int r, c, i, j, k;
   	cin>>r>>c;

   	char mat[r][c];

   	for(i=0; i<r; i++) scanf("%s\n",mat[i]);




   for(i=0; i<r; i++)
   {
   	for(j=0; j<c; j++)
   	{
   		if(mat[i][j]!='?')
   		{
   			bool flag=false;
   			for(k=j+1; k<c && mat[i][k]=='?'; k++)
   			{
   				mat[i][k]=mat[i][j];

   			}

   			for(k=j-1; k>=0 && mat[i][k]=='?'; k--)
   			{
   				mat[i][k]=mat[i][j];

   			}
   		}
   	}
   }


for(j=0; j<c; j++)
   {
   	for(i=0; i<r; i++)
   	{
   		if(mat[i][j]!='?')
   		{
   			bool flag=false;
   			for(k=i+1; k<r && mat[k][j]=='?'; k++)
   			{
   				mat[k][j]=mat[i][j];

   			}

   			for(k=i-1; k>=0 && mat[k][j]=='?'; k--)
   			{
   				mat[k][j]=mat[i][j];

   			}
   		}
   	}
   }


    
   for(i=0; i<r; i++) 
   {
   	for(j=0; j<c; j++)
   		 cout<<mat[i][j];
   	cout<<endl;
   }



   }

   return 0;
}

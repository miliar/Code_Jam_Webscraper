#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;
 
typedef long long int lli;
typedef unsigned long long ull;
typedef long double ld;
typedef vector <long long> vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector <int> vii;
typedef complex <double> Point;
 
#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
 
long long t, n, m, u, v, q, k;
const int N = 2e5 + 500;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 57;
 
long long arr[N];
string str, ss;
bool tidy(lli b[18],int index)
{
  int i=0,f=0;
  for(i=0;i<index-1;i++)
  {
   if(b[i]<=b[i+1])continue;
   else{f=1;break;}
  }
  if(f==1)return false;
  if(b[index-1]!=0) return true;
  return false;
}
void print(lli b[18],lli index)
{
 int begin=0;
 for(int i=0;i<index;i++)
 { 
  if(begin==0)//hasnt begun yet
  {
    if(b[i]==0)continue;
	else{if(b[i]!=0) {begin++;cout<<b[i];} }
  }
  else
  { 
    cout<<b[i];
  }
 }
}
int main() {
   csl;
	int testcases;cin>>testcases;
   for(int loop=1;loop<=testcases;loop++)
   {
    lli n,i,j,index=0,arr[18],b[18];
	cin>>n;
	lli copy=n;//15523
	int nod=0;
	while(copy!=0)
	{
	  int d=copy%10;
	  arr[index++]=d;
	  
	  copy/=10;
	}//NOW ARRAY HAS 3 2 5 5 1 and index=5
	int ind=0;
	for(i=index-1;i>=0;i--)
	{
	 b[ind++]=arr[i];
	}
	nod=index;//NUMBER OF DIGITS
	//now array b  has the number N 1 5 5 2 3 and ind=5
	if(tidy(b,nod)){cout<<"Case #"<<loop<<": ";print(b,ind);cout<<"\n";continue;}
	/*if(b[0]==1)//THAT CASE
	{
	
	  
	}//end of that case
	*/
	//JUST A SIMPLE CASE
	int f=0;
	for(i=0;i<nod-1;i++)
	{
	  if(b[i]<=b[i+1])
	  {continue;
	  }
	  else
	  {  
	    if(b[i]>1)
			{int val=b[i];b[i]--;
			 for(j=i-1;j>=0;j--)
			 {
			  if(b[j]==val){b[j]--;b[j+1]=9;}
			 }
			 for(j=i+1;j<nod;j++)
			 { 
			   b[j]=9;
			 }
			 f=1;break;
			}
		else
		{
		  b[0]=0;
		  for(j=1;j<nod;j++)b[j]=9;
		  f=1;break;
		}
	  }
	}//end of for loop
    cout<<"Case #"<<loop<<": ";print(b,nod);cout<<"\n";continue;
    }//end of testcases    
}//end of main
 
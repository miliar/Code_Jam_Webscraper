#include <bits/stdc++.h>
using namespace std;
int mypowerfun(int arr,int b)
{
	if(b==0)
	return 1;
	if(b==1)
	return arr;
	int x=mypowerfun( arr,b/2);
	if(b%2==0)
	return x*x;
	else
	return x*x*arr;
}
void pri_arr(int arr[],int n )
{
   int i;
   for(i=0;i<n;i++)
	  printf("%d ",arr[i]);
   printf("\n");
}
void pri_vec(vector<int> a,int n)
{
for (std::vector<int>::iterator it = a.begin() ; it != a.end(); ++it)
    std::cout  << *it;
  std::cout << '\n';
}
int mygcd(int arr,int b)
{
	if (b != 0)
       return mygcd(b, arr%b);
    else
       return arr;
}
#define pb push_back
#define mp make_pair
typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;
const ll INF= ll (1e18);
const int MOD= 1e9+7;
unsigned long long functio(string st);
int main() {
    freopen("input.in","r",stdin);
freopen("output_file_name.out","w",stdout);
	int t;cin>>t;
	for (int tcases=1;tcases<=t;tcases++)
	{
	    string numbers;cin>>numbers;
	    int flg=0;
	    if (numbers.size()==1)
	    {
	        cout<<"Case #"<<tcases<<": "<<numbers<<endl;continue;
	    }
	    for (int i=1;i<numbers.size();i++)
	    {
	    	if (numbers[i]<numbers[i-1])
	    	{
	    		flg=1;break;
	    	}
	    }
	    if (flg==0)
	    cout<<"Case #"<<tcases<<": "<<functio(numbers)<<endl;
	    else
	    {
	    	for (int i=0;i<numbers.size()-1;i++)
	    	{if (numbers[i]>=numbers[i+1])
	    	    {
	    	        numbers[i]=numbers[i]-1;
	    	        for (int j=i+1;j<numbers.size();j++)
                            numbers[j]='9';
		            break;
	    	    }
	    	}
	    	cout<<"Case #"<<tcases<<": "<<functio(numbers)<<endl;
	    }
	}
	return 0;
}
unsigned long long functio(string st)
{
       unsigned long long n=0,i=0;
        while(st[i]!='\0') {
                n=n*10+((int)st[i]-48); i++;
        }
        return n;
}

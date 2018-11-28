#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define fast ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl '\n'
#define pb push_back
#define mp make_pair
#define full(a) a.begin(),a.end()
#define mem(a,x) memset(a,x,sizeof(a))
#define test int t;cin>>t; while(t--)
#define MOD 1000000007

using namespace std;

ll brute(ll n) //Checker
{
	for(ll i = n;i>=0 ; --i)
	{
		bool tidy = true; 
		ll temp = i;
		ll prev = temp%10;
		temp/=10;
		while(temp)
		{
			if((temp%10)>prev) 
			{
				tidy=false;
				break;
			}
			prev= temp%10;
			temp/=10;
		}
		if(tidy)
		{
			//cout<<"Case #"<<++hmm<<": ";
			return i;
		}
	}	
}

string stringConvert(ll n)
{
	string ans="";
	while(n)
	{
		ans = (char)(n%10+48) + ans;
		n/=10;
	}
	return ans;
}

ll longlongConvert(string x)
{
	ll ans = 0;
	for(int i=0;i<x.length();i++)
	{
		ans = ans*10 + (x[i]-48);
	}
	return ans;
}

string adhoc(string s)
{
	int l = s.length();
	bool smaller = false; 
	int smallerPossibleIndex  = -1; 
	char value ;
	for(int i=0;i<l;i++)
	{
		if(i+1<l &&( (s[i]>'1' && s[i] > s[i+1])  || (s[i]=='9' && s[i+1]=='9') ) )
		{
			value = s[i];
			smallerPossibleIndex = i;
			break;
		}
		else if (i+1<l &&( (s[i]=='1' && s[i] > s[i+1]) ) )
		{
			smallerPossibleIndex = -1;
			break;
		}
	}
	if(smallerPossibleIndex==-1)
	{
		string ans="";
		for(int i=0;i<l-1;i++) ans+="9";
		return ans;
	}
	int index = smallerPossibleIndex - 1;
	while(s[index]==value)
	{
		index--;
	}
	smallerPossibleIndex= index+1;
	for(int i=0;i<l;i++)
	{
		if(i==smallerPossibleIndex)
		{
			s[i]=s[i]-1;
		}
		else if(i>smallerPossibleIndex)
		{
			s[i] = '9';
		}
	}
	return s;
}

bool increasing(string s)
{
	int prev = s[0]-48;
	for(int i=1;i<s.length();i++)
	{
		if((s[i]-48) < prev) return false;
		prev = s[i]-48;
	}
	return true;
}

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	//srand(time(NULL));
	int t;
	cin>>t;
	int hmm = 0;
	while(t--)
	{
		ll n;
		cin>>n;
		string nstring = stringConvert(n);
		cout<<"Case #"<<++hmm<<": ";
		if(increasing(nstring))
		{
			cout<<n<<endl;
		}
		else
		{
			string ans = adhoc(nstring);
			cout<<longlongConvert(ans)<<endl;	
		}	
	}	
}

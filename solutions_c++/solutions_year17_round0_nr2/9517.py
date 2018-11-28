# include <bits/stdc++.h>
using namespace std;

void eval()
{
	long long n;
	cin>>n;
	while(n)
	{
		long long arr[4] = {0};
		int i = 0;
		int j = 0;
		long long temp = n;
		while(temp)
		{
			long long x = temp % 10;
			arr[i] = x;
			temp = temp/10;
			i++;	
		}
		//j = i-1;
		//cout<<j<<" ";
		long count = 0;
		while(j<i-1 && arr[j]>=arr[j+1] )
		{
			count++;
			j++;
		}
			
		if(count == i-1)
		{
			cout<<n<<endl;
			return;
		}
		n--;	
	}
	
}

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++)
	{
		cout << "Case #" << tt << ": ";
		eval();
	}
    return 0;
}

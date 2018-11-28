#include<bits/stdc++.h>
#define ll long long 

using namespace std;

int main()
{
	string s;int k;
		
	FILE *fp = fopen("output.txt" , "w+");
	int T;cin >> T;
	for(int I = 1;I <= T;I++)
	{
		ll int n;
		cin >> n;

		int x = 0;
		int a[50];
		memset(a , 0 , sizeof(a));
		while(n > 0)
		{
			int d = n % 10;
			a[x++] = d;
			n /= 10;
		}
		for(int i = 0;i < x / 2;i++)	swap(a[i] , a[x - i - 1]);
		//for(int i = 0;i < x;i++)	cout << a[i];

		if(x == 1){	fprintf(fp , "Case #%d: %d\n" , I , a[0]);continue;}

		//TWO POINTERS
		//backward direction
		for(int right = x - 1 , left = x - 2;left >= 0;)
		{
			if(a[left] > a[right])
			{
				a[left]--;
				a[right] = 9;
				left--;
				right--;
			}
			else
			{
				left--;right--;
			}
		}
		int pos = 0;
		for(int i = 0;i < x;i++)	if(a[i]){pos = i;break;}
		//for(int i = pos;i < x;i++)		cout << a[i];cout << endl;
		//forward direction
		for(int right = pos + 1 , left = pos;right < x;)
		{
			if(a[left] > a[right])
			{
				a[right] = a[left];
				left++;right++;
			}
			else
			{
				right++;left++;
			}
		}
		ll int number = 0;
		for(int i = pos;i < x;i++)		number = number * 10 + a[i];
		//cout << number << "\n";
		fprintf(fp , "Case #%d: %lld\n" , I , number);
	}
}

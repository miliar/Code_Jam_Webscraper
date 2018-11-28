#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("output.txt","w",stdout);

	int test;
	cin >> test;

	int cnt=1;

	while(test--)
	{
		long long int N;
		cin >> N;
		int flag = 0;
		if(N<10)
		{
			cout << "Case #"<<cnt<<": "<< N << endl;
			flag = 1;
		}
		if(flag==0)
		{
			long long size = log10(N)+1;
			long long array1[size],array2[size];
			for(int i=size-1;i>=0;i--)
			{
                array1[i] = N%10;
				N = N/10;
			}
			for(int i=0;i<size;i++)
			{
				array2[i] = array1[i];
			}
			/*
			for(int i=0;i<size;i++)
				cout << array1[i] << " ";
			*/
			while(1)
			{
				if(is_sorted(array2,array2+size))
					break;
				for(int i=0;i<size-1;i++)
				{
					if(array2[i]>array2[i+1])
					{
						array2[i]=array2[i]-1;
						for(int z=i+1;z<size;z++)
							array2[z]=9;
					}
				}
			}
			cout<<"Case #"<<cnt<<": ";
			if(array2[0]!=0)
					cout << array2[0];

			for(int i=1;i<size;i++)
				cout<<array2[i];
			cout << endl;
		}
		cnt++;
	}

	return 0;
}


#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main() {

	int t;
	cin>>t;
	for (int i1 = 1; i1<= t; ++i1) 
	{
		int n;
		int *arr;
		cin >>n;
		arr = new int[n];

		for (int i = 0; i < n; ++i)
		{
			arr[i] = -1;
			/* code */
		}

		int arr_color[6] = {0,0,0,0,0,0};


		for (int i = 0; i < 6; ++i)
		{
			cin>>arr_color[i];
		}

		int imposs = 0;
		for (int i = 0;i<6;i++) {
			if (arr_color[i]>n/2)
			{
				imposs = 1;
				break;
			}
		}
		if (imposs == 1)
		{
			cout <<"Case #"<<i1<<": IMPOSSIBLE\n";
		}
		else {
			int maxInd1 = 0;
			for (int i = 0; i < 6; ++i)
			{
				if (arr_color[i] > arr_color[maxInd1])
				{
					maxInd1 = i;
				}

			}
			int maxInd2 = (maxInd1 + 1)%6;
			for (int i = 0; i < 6; ++i)
			{
				if (arr_color[i] > arr_color[maxInd2] && maxInd1!=i)
				{
					maxInd2 = i;
				}

			}

			int maxInd3;
			if (maxInd1!=0 && maxInd2!=0)
			{
				maxInd3 = 0;
			}

			else if (maxInd1!=2 && maxInd2!=2) {
				maxInd3 = 2;
			}
			else {
				maxInd3 = 4;
			}

			int count = 0;
			int i = 0;
			while (1) {
				if (count>=arr_color[maxInd1])
				{
					break;
				}
				arr[i] = maxInd1;
				count++;
				i+=2;
			}

			i--;
			count = 0;
			while(1) {
				if (count>=arr_color[maxInd2]) {
					break;
				}
				if (i>=n)
				{
					i=1;
				}
				arr[i] =maxInd2;
				count++;
				i+=2;
			}


			for (int i = 0; i < n; ++i)
			{
				if (arr[i] == -1)
				{
					arr[i] = maxInd3;
					/* code */
				}
				/* code */
			}


			cout <<"Case #"<<i1<<": ";
			for (int i = 0; i < n; ++i)
			{
				switch(arr[i]) {
					case 0:
					cout <<"R";
					break;
					case 2:
					cout<<"Y";
					break;
					case 4:
					cout<<"B";
					break; 
				}
				/* code */
			}
			cout<<endl;}
	
		}

	return 0;
}

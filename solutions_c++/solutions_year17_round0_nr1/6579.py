#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;


bool check(string arr){


	
	for (int i = 0; i < arr.length(); i++)
	{

		if (arr[i] =='-')
			return true;
	}

	return false;

}


void fun(string& arr, int i, int k){

	int j = i + k;

	for ( ; i < j; i++){


		if (arr[i] == '-')
			arr[i] = '+';
		else
		arr[i] = '-';


	}
	

}


int main(){



	ifstream cin;
	ofstream cout;
	cout.open("out.txt");
	cin.open("A-large.in");

	if (cin){
		int t = 0;
		cin >> t;

		for (int i = 1; i <= t; i++)
		{


			string arr;
			cin >> arr;


			int k = 0;
			cin >> k;

			
			int count = 0;



			for (int i = 0; i <= arr.length() - k; i++)
			{

				if (arr[i] == '-'){
					fun(arr, i, k);
					count++;

				}
				else if (!check(arr))
					break;
			}

			if (check(arr)){


				cout << "Case #" << i << ": IMPOSSIBLE" << endl;


			}
			else
				cout << "Case #" << i << ": " << count << endl;
		}

	}













	return 0;
}
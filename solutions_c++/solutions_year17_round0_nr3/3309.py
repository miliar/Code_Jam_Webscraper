//#include<iostream>
//#include<stdlib.h>
//
//using namespace std;
//
//int T;		//Testcase
//long long N;		//Maxmum number
//int * NArr;	//
//int l;		//length of Number
//bool tidy;
//
//void ChangeToArray(){
//	long long temp = N;
//
//	l = 1;
//	
//	while ((temp/=10) != 0)
//		l++;
//
//	NArr = new int[l];
//
//	temp = N;
//	for (int i = l-1; i > -1 ; i--)
//	{
//		NArr[i] = temp%10;
//		temp /= 10;
//	}
//}
//
//void cal()
//{
//	int idx = 0;
//	tidy = true;
//
//	for (int i = 0; i < l-1; i++)
//	{
//		if (NArr[i] > NArr[i+1])
//		{
//			idx = i;
//			tidy = false;
//			break;
//		}
//	}
//
//	if (tidy == false)
//	{
//		for (int i = idx; i>=0; i--)
//		{
//			if (NArr[i] != NArr[i - 1])
//			{
//				idx = i;
//				break;
//			}
//		}
//		NArr[idx] -= 1;
//
//		for (int i = idx + 1; i < l; i++)
//		{
//			NArr[i] = 9;
//		}
//
//	}
//
//
//	for (int i = 0; i < l; i++){
//		if (NArr[i] == 0)
//			continue;
//		printf("%d", NArr[i]);
//	}
//	printf("\n");
//}
//
//int main(){
//	scanf_s("%d", &T);
//
//	for (int i=1; i < T+1;i++)
//	{
//		scanf_s("%lld", &N);
//		ChangeToArray();
//		printf("Case #%d: ", i);
//		cal();
//	}
//
//	return 0;
//}

#include<iostream>
int T;
long long N, K;
int a;
long long large; 
long long small;
long long numberOfLarge;		
long long idx;
long long min, max;
long long temp;

using namespace std;

void SetA()
{
	temp=1;
	
	for (int i = 0; i < 60; i++)
	{
		if (temp > K)
		{
			a = i-1;
			temp /= 2;
			return;
		}
		temp *= 2;
	}
}

void SetLarge()
{
	small = (N - temp + 1) / temp;
	if (((N - temp + 1) % temp) == 0)
		large = small;
	else
	{
		large = small+1;
	}
}

void SetNumberOfLarge()
{
	numberOfLarge = N - temp*large + 1;
}

void SetIdx()
{
	idx = K - temp;
}

void finalCalculate()
{
	if (++idx <= numberOfLarge)
	{
		if (large % 2 == 0)
		{
			min = large / 2-1;
			max = large / 2;
		}
		else
		{
			min = max = (large - 1) / 2;
		}
	}
	else
	{
		if (small % 2 == 0)
		{
			min = small / 2-1;
			max = small / 2;
		}
		else
		{
			min = max = (small - 1) / 2;
		}
	}
}

void SetAll()
{
	SetA();
	SetLarge();
	SetNumberOfLarge();
	SetIdx();


}

int main()
{
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> N;
		cin >> K;
		SetAll();
		finalCalculate();
		cout << "Case #" << i+1 << ": " << max << " " << min<<endl;
	}

	return 0;
}
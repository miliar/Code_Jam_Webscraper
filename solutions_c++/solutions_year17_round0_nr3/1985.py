#include <iostream>

int T;
long long N, K;
int a;
long long large; 
long long small;
long long numberOfLarge;		
long long idx;
long long min, max;
long long temp;

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
	std::cin >> T;
	for (int i = 0; i < T; i++)
	{
		std::cin >> N;
		std::cin >> K;
		SetAll();
		finalCalculate();
		std::cout << "Case #" << i+1 << ": " << max << " " << min<<std::endl;
	}

	return 0;
}
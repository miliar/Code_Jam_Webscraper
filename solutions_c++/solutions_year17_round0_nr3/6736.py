#include<iostream>
#include<climits>
using namespace std;

void showStall(bool stall[],int n)
{
	for(int i=0; i<n; i++)
	{
		if(stall[i])
		{
			cout << 'O' ;
		}
		else
			cout << '.' ;
	}
	cout << endl;
	return ;
}

int max(int a, int b)
{
	if(a>b)
	{
		return a;
	}
	else
		return b;
}

int min(int a, int b)
{
	if(a<b)
	{
		return a;
	}
	else
		return b;
}

int tmpVal;
int count;
int index;

int main()
{
	int t;
	cin >> t;
	int n,k;
	for(int i=0; i<t; i++)
	{
		//setup
		cin >> n >> k ;
		bool stall[n+2];
		int valStall[n+2][4];
		stall[0] = true ;
		for(int j=1; j<=n; j++)
		{
			stall[j] = false;
		}
		stall[n+1] = true;
	//	showStall(stall,n+2);
		
		int ls,rs;
		bool markMAXmin[n+2];
		
		//find LsRs
		for(int lap = 0; lap < k; lap++)
	{
		for(int j=1; j<=n; j++)
		{
		//	cout << '{' << j << '}' << ' ' ;
			if(stall[j]==false)
			{
				valStall[j][0] = 0;
				valStall[j][1] = 0;
				for(int k=j-1; k>0; k--)
				{
					if(stall[k])
					{
						break;
					}
					valStall[j][0]++;
				}
				for(int k=j+1; k<=n; k++)
				{
					if(stall[k])
					{
						break;
					}
					valStall[j][1]++;
				}
				valStall[j][2] = min(valStall[j][0],valStall[j][1]);
				valStall[j][3] = max(valStall[j][0],valStall[j][1]);
			}
	//		cout << '[' << valStall[j][0] << ']' << '[' << valStall[j][1] << ']' << '[' << valStall[j][2] << ']' << '[' << valStall[j][3] << ']' << endl;
		}
		//find MaxOfMin
		tmpVal = INT_MIN;
		count = 0;
		for(int j=1; j<=n; j++)
		{
			if(!stall[j])
			{
				if(valStall[j][2]>tmpVal)
				{
					tmpVal = valStall[j][2];
				}
			}
		}
		// mark MAXmin
		for(int j=1; j<=n; j++)
		{
			markMAXmin[j] = false;
		}
		for(int j=1; j<=n ;j++)
		{
			if(!stall[j])
			{
				if(valStall[j][2]==tmpVal)
				{
					markMAXmin[j] = true;
					count++;
					index = j;
				}
			}
		}
	//	cout << "LastMin = " << tmpVal << '[' << index << ']' << count << endl; 
		// First Condition
		if(count==1)
		{
			stall[index] = true;
		}
		else
		{
	//		cout << "Min is not one" << endl;
			tmpVal = INT_MIN;
			for(int j=1; j<=n; j++)
			{
				if(markMAXmin[j])
				{
					if(valStall[j][3]>tmpVal)
					{
						tmpVal = valStall[j][3];
					}
				}
			}
	//		cout << "Max of Max = " << tmpVal << endl;
			for(int j=1; j<=n; j++)
			{
				if(markMAXmin[j])
				{
					if(valStall[j][3]==tmpVal)
					{
						stall[j] = true;
						index = j;
						break;
					}
				}
			}
		}
	//	showStall(stall,n+2);
	}
	cout << "Case #" << i+1 << ": " << valStall[index][3] << ' ' << valStall[index][2] << endl;
	}
	return 0;
}

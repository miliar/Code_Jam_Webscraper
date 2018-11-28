#include <bits/stdc++.h>

using namespace std;

struct value
{
	int minore = 1000000, maggiore = 0;	
};

int binary_search(int N, vector<int> A, int X)
{
	int low = 0, high = N-1;
	
	while(low <= high)
	{
		int mid = (low+high)/2;
		if(A[mid] == X)
			return mid;
		else if(A[mid] < X)
			low = mid+1;
		else if(A[mid] > X)
			high = mid-1;
	}
	
	return -1;
}

value sol(int N, int K)
{
	value solution;
	
	vector<int> posizioni;
	posizioni.push_back(0);
	posizioni.push_back(N+1);
	
	int ultimo;
	
	for(int i = 0; i < K; i++)
	{
		int maggiore = 0;
		int indice = 30;
		for(int j = 1; j < posizioni.size(); j++)
		{
			if(posizioni[j] - posizioni[j-1] > maggiore)
			{
				maggiore = posizioni[j] - posizioni[j-1];
				indice = (posizioni[j]+posizioni[j-1])/2;
			}
		}
		
		ultimo = indice;
		
		posizioni.push_back(indice);
		sort(posizioni.begin(), posizioni.end());
	}
	
	ultimo = binary_search(posizioni.size(), posizioni, ultimo);
	
	if(posizioni[ultimo] - posizioni[ultimo-1]-1 > solution.maggiore)
		solution.maggiore = posizioni[ultimo] - posizioni[ultimo-1]-1;
	if(posizioni[ultimo+1] - posizioni[ultimo]-1 > solution.maggiore)
		solution.maggiore = posizioni[ultimo+1] - posizioni[ultimo]-1;

	if(posizioni[ultimo] - posizioni[ultimo-1]-1 < solution.minore)
		solution.minore = posizioni[ultimo] - posizioni[ultimo-1]-1;
	if(posizioni[ultimo+1]-posizioni[ultimo]-1 < solution.minore)
		solution.minore = posizioni[ultimo+1]-posizioni[ultimo]-1;
	
	return solution;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.in", "w", stdout);
	
	int T;
	cin >> T;
	
	for(int i = 0; i < T; i++)
	{
		int N, K;
		cin >> N >> K;
		
		value soluzione = sol(N, K);
		
		cout << "Case #" << i+1 << ": " << soluzione.maggiore << " " << soluzione.minore << endl;
	}
	
	return 0;
}

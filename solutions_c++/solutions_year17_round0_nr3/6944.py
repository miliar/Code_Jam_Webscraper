#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<queue>

using namespace std;
void sert(int start, int end, int** &first)
{
	int insert =start+ (end - start) / 2;
	
	
	first[0][0] = start;
	first[0][1] = insert - 1;
	first[1][0] = insert + 1;
	first[1][1] = end;

}

int* ins(int N,int K)
{
	int finalresult[2];
	map<int,queue<int*>> q;
	int firstzone[2] = { 0, N - 1 };
	
	queue<int *> first;
	first.push(firstzone);
	q.insert(make_pair(N - 1, first));
	for (int i = 0; i < K; i++)
	{
		auto x = std::max_element(q.begin(), q.end(), q.value_comp());
		
		int * take = x->second.front();
		x->second.pop();
		if (x->second.size() == 0) q.erase(x);
		if (take[1] - take[0] <= 0)
		{ //直接返回最后结果，停止迭代
			finalresult[0] = 0;
			finalresult[1] = 0;
			return finalresult;
		}
		int **result=new int*[2];
		result[0] = new int[2];
		result[1] = new int[2];
		sert(take[0], take[1], result);
		
		finalresult[0] = result[0][1] - result[0][0] + 1;
		finalresult[1] = result[1][1] - result[1][0] + 1;
		
		if(finalresult[0]>0)q[finalresult[0]].push(result[0]);
		if (finalresult[1] > 0)q[finalresult[1]].push(result[1]);
	}
	return finalresult;

}
int main()
{
	int N;
	cin >> N;
	ofstream haha("test.txt");
	for (int i = 1; i <= N; i++)
	{
		int X, K;
		cin >> X >> K;
		int* result = ins(X, K);
		haha << "Case #"<<i<< ": "<<result[1] << " " << result[0] << endl;

	}
}
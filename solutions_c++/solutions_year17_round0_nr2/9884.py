//#include <iostream>
//#include <algorithm>
//#include <vector>
//#include<stack>
//
//using std::vector;
//using std::pair;
//using std::stack;
//
//vector<bool>visited;
//vector<bool>processed;
//vector<int>post;
//vector<int>pre;
//stack<int>s;
//
//int clk = 1;
//void explore(vector<vector<int> > &adj, int v){
//	visited[v] = true;
//	pre[v] = clk++;
//	for (int i = 0; i < adj[v].size(); i++){
//		if (!visited[adj[v][i]]){
//			explore(adj, adj[v][i]);
//		}
//
//	}
//
//	post[v] = clk++;
//	s.push(v);
//
//}
//void DFS(vector<vector<int> > &adj){
//	for (int i = 0; i < adj.size(); i++){
//		if (!visited[i]){
//			explore(adj, i);
//		}
//	}
//
//
//}
//
//
//void dfs(vector<vector<int> > &adj, vector<int> &used, vector<int> &order, int x) {
//	//write your code here
//}
//
//vector<int> toposort(vector<vector<int> >& adj) {
//	//vector<int> used(adj.size(), 0);
//	//vector<int> order;
//	DFS(adj);
//	vector<int>order(adj.size());
//	for (int i = 0; i < adj.size(); i++){
//		order[i] = s.top();
//		s.pop();
//	}
//	//write your code here
//	return order;
//}
//
//int main() {
//	size_t n, m;
//	std::cin >> n >> m;
//
//	vector<vector<int> > adj(n, vector<int>());
//	visited.resize(n);
//	post.resize(n);
//	pre.resize(n);
//
//	for (size_t i = 0; i < m; i++) {
//		int x, y;
//		std::cin >> x >> y;
//		adj[x - 1].push_back(y - 1);
//	}
//	for (int i = 0; i < n; i++){
//		visited[i] = false;
//		processed[i] = false;
//	}
//	vector<int> order = toposort(adj);
//	for (size_t i = 0; i < order.size(); i++) {
//		std::cout << order[i] + 1 << " ";
//	}
//	system("pause");
//}
#include<iostream>
#include<string>
#include<vector>
using namespace std;
unsigned long long getTidyNum(unsigned long long n){
	/*int c;
	if (n == 111111111111108553){
		c = 1;
	}*/
	 unsigned long long temp = n;
	vector<int>digits;
	bool isTidy = true;
	for (int i = 0; temp > 0;i++){
		digits.push_back( temp % 10);
		temp = temp / 10;
	}
	int max = digits[0];
	for (unsigned long long i = 1; i <digits.size(); i++){
		if (digits[i] >max){
			isTidy = false;
			//cout << n - 1<<"\n";
			return getTidyNum(n - 1);
		}
		else
			max = digits[i];
	}
	if (isTidy)
		return n;
}
vector<unsigned long long>solve(vector<unsigned long long>&vec){
	vector<unsigned long long> result(vec.size());
	for (int i = 0; i < vec.size(); i++){
		result[i] = getTidyNum(vec[i]);
	}
	return result;
}

int main(){
	freopen("in.txt", "r", stdin);

	
	freopen("out.txt", "w", stdout);
	int n;
	
	cin >> n;
	vector<unsigned long long>vec(n);
	for (int i = 0; i < n; i++){
		cin >> vec[i];
	}
	vector<unsigned long long>result = solve(vec);
	//output
	for (int i = 0; i < n; i++){
		cout << "Case #"<<i+1<<": "<<result[i]<<"\n";
		
	}
	/*unsigned long long n;
	cin >> n;
	cout << getTidyNum(n);

	system("pause");*/
}
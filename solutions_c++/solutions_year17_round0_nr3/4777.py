#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>
using namespace std;
template<typename T> priority_queue<int> print_queue(T& q) {
    std::priority_queue<int> z;
    while(!q.empty()) {
        std::cout << q.top() << " ";
        z.push(q.top());
        q.pop();
    }
    std::cout << '\n';
    return z;
}
string solve(int a,int b){
    std::priority_queue<int> q;
    q.push(a);
    int n;
    for(int _=0;_<b;_++){
        n=q.top();
        q.pop();
        q.push((n-1)/2);
        q.push(n/2);
        //q=print_queue(q);
    }
    return std::to_string(n/2)+" "+std::to_string((n-1)/2);

}


int main() {
    int test_cases;
	cin >> test_cases;
	for (int test_case = 1; test_case <= test_cases; test_case++) {
		int a;
		cin >> a;
		int b;
		cin >> b;
		cout << "Case #" << test_case << ": " << solve(a,b) << endl;
		cout.flush();
		cerr<<test_case<< endl;
	}
	return 0;
}

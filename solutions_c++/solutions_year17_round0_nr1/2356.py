#include <iostream>
#include <queue>
#include <string>

int T=0, K=0;
std::queue<int> q;
std::string s;

using namespace std;

int is_happy(int pos) {
    return (q.size() + (('+'==s[pos]) ? 1 : 0)) % 2;
}

int solve(const string& s) {
    std::queue<int>().swap(q);
    int L = s.size();
    int f = 0;

    for (int j=L-1; 0<=j; --j) {
    	while ((! q.empty()) && (j < q.front()))
            q.pop();
        
	if (! is_happy(j)) {
	    if (K <= j+1) {
                q.push(j+1-K);
                ++f;
	    } else
                return -1;
        }
    }

    return f;
}

int main() {
    cin >> T;
    
    for (int i=0; i<T; ++i) {
        s.clear();
    
        cin >> s;
        cin >> K;

        cout << "Case #" << (1+i) << ": ";
        //cout << s << "#" << endl;
        //cout << "K=" << K << endl;

	int f = solve(s);
	if (-1 == f)
	    cout << "IMPOSSIBLE";
        else
            cout << f;

	cout << endl;
    }

    return 0;
}

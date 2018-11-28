#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<bool> s_to_array(string s)
{
    vector<bool> a;

    for(char& c : s) {
        a.push_back(c == '+' ? true : false);
    }

    return a;
}

string run_test(string s, int k)
{
    auto n = 0;
    auto a = s_to_array(s);
    for(int i = 0; i <= a.size() - k; i++) {
        if (!a[i]) {
            for(int j = i; j < i+k; j++)
                a[j] = !a[j];
            n++;
        }
    }
    
    for(int i = a.size() - k + 1; i < a.size(); i++) {
        if (!a[i]) {
            return "IMPOSSIBLE";
        }
    }

	return to_string(n);
}

int main()
{
	string line;
	cin>>line;

	auto n_tests = stoi(line);	

	for(int i = 0; i < n_tests; i++) {
        string s;
        int k;
		cin>>s;
		cin>>k;

		cout<<"Case #"<<i+1<<": ";

		auto result = run_test(s,k);

		cout<<result<<"\n";	
	}
}

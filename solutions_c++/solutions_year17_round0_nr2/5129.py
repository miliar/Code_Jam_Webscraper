#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int find_untidy(vector<int> a)
{
    for(int i = 0; i < a.size() - 1; i++) {
        if(a[i] > a[i+1])
            return i+1;
    }

    return -1;
}

vector<int> decimalstring_to_array(string s)
{
    vector<int> a;
    for(char& c : s) {
        a.push_back(c-0x30);
    }
    return a;
}

string array_to_decimalstring(vector<int> a)
{
    bool trim_zeroes = true;
    stringstream s;
     for(int& i : a) {
        if (i==0 && trim_zeroes)
            continue;

        s << (char)(i+0x30);
        trim_zeroes = false;
    }
    return s.str();
}

void tidy(vector<int>& a, int untidy)
{
    for(int i = untidy; i < a.size(); i++) {
        a[i] = 9;
    }

    for(int i = untidy-1; i >= 0; i--) {
        if (a[i] > 0) {
            a[i] = a[i]-1;
            return;
        }
        a[i] = 9;
    }
}

string run_test(string s)
{
    auto a = decimalstring_to_array(s);    
    
    while(1) {
        auto x = find_untidy(a);
        if (x == -1)
            return array_to_decimalstring(a);
        
        tidy(a, x);
    }
}

int main()
{
	string line;
	cin>>line;

	auto n_tests = stoi(line);	

	for(int i = 0; i < n_tests; i++) {        
        string n;
		cin>>n;

		cout<<"Case #"<<i+1<<": ";

		auto result = run_test(n);

		cout<<result<<"\n";	
	}
}

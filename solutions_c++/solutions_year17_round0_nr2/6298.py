#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <list>
#include <math.h>

using namespace std;

unsigned long long int transform_tidy(unsigned long long int n){
    if (n <10) {
        return n;
    }
	stack<int> temp;
	list<int> original;

    while(n > 0) {
		int r = n % 10;
//        cout<<r;
		original.push_back(r);
		n = n/10;
	}


    while(!original.empty()) {
        int t = 0;
        int o = 0;
        if (temp.empty()) {
            o = original.front();
            original.pop_front();
            temp.push(o);
        }
        o = original.front();
        original.pop_front();
        t = temp.top();
        temp.pop();
        if (o > t) {
            o = o - 1;
            t = 9;
            original.push_front(o);
            original.push_front(t);
            while(!temp.empty()) {
                temp.pop();
                original.push_front(9);
            }
        }
        else {
            temp.push(t);
            temp.push(o);
        }
    }


	unsigned long long int m = 0;
	while(!temp.empty()) {
		m = m * 10 + temp.top();
		temp.pop();
	}

	return m;
}

int main() {
	int t;
	cin>>t;
	unsigned long long int n;
	int i = 1;
	while(t--) {
		cin>>n;
		cout<<"Case #"<<i<<": "<<transform_tidy(n)<<endl;
		i++;
	}
	return 0;
}
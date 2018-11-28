#include <iostream>
#include <fstream>
#include <queue>
#define LL long long
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open ("C-small-2-attempt0.in");
	out.open ("output.txt");
	
	int t;
	in >> t;
	for(int i=1; i<=t; i++){
		//cout << "i = " << i << endl;
		LL n; LL k;
		in >> n >> k;
		//cout << "n = " << n << " k = " << k << endl;
		priority_queue<int> my_queue;
		my_queue.push(n);
		int a; int b;
		for(int j=0; j<k; j++){
			int tmp = my_queue.top() - 1; my_queue.pop();
			a = (int)tmp / 2 + tmp % 2;
			b = (int)tmp / 2;
			//cout << "a = " << a << " b = " << b << endl;
			my_queue.push(a); my_queue.push(b);
		}
		out << "Case #" << i << ": " << a << " " << b << endl;
	}
	
    in.close();
    out.close();
    return 0;
}

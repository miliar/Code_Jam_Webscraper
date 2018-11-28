#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <queue>

using namespace std;

template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}

string optimized(int stalls, int k) {
	int c;

	std::priority_queue<int> q;
	q.push(stalls);
	// print_queue(q);

	for(int i=0; i<k-1; i++) {
		c = q.top();
		q.pop();
		if (c > 2) {
			q.push(c/2);
			q.push((c-1)/2);
		} else {
			if (c == 2) {
				q.push(1);
			}
		}
	}

	// print_queue(q);
	c = q.top();
	q.pop();
	if (c > 2) {
		return std::to_string(c/2)+" "+std::to_string((c-1)/2);
	} else {
		if (c == 2) {
			return "1 0";
		} else {
			return "0 0";
		}
	}
}

int main () {

	ifstream infile("C-small-2-attempt2.in");

	// ifstream infile("input");
	ofstream outfile("output");
	std::string line;
	int n,a,b;

	std::getline(infile, line);
	std::stringstream ss;
	ss.str(line);
	ss>>n;

	for(int i=0;i<n;i++) {
		std::getline(infile, line);
		std::stringstream ss;
		ss.str(line);
		ss>>a;
		ss>>b;
		outfile<<"Case #"+std::to_string(i+1)+": "+optimized(a,b)+"\n";
		// cout<<"Time taken: "<<std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC)<<"s for "<<i<<endl;
	}
	outfile.close();
	infile.close();
    return 0;
}

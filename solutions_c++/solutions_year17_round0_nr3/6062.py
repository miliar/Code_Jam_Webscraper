// ConsoleApplication6.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <queue>

using namespace std;

class a {
	public:
	int start;
	int length;
	a() {}
	a(int s, int l) {
		start = s;
		length = l;
	}
};

struct cmp {
	bool operator()(a t, a u) {
		if (t.length < u.length) return true;
		else if (t.length == u.length) return t.start > u.start;
		else return false;
	}
};


int main()
{
	ios::sync_with_stdio(false);
	ofstream outFile("output.txt");

	int T=1;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		
		int N, K;
		cin >> N;
		cin >> K;

		priority_queue<a, vector<a>, cmp> pq;

		a tmp;
		pq.push(a(0, N));
		for (int j = 1; j <= K; j++) {
			tmp = pq.top();
			pq.pop();

//			cout << tmp.start << ' ' << tmp.length << "pop" << endl;

			pq.push( a(tmp.start, (tmp.length - 1) / 2) );
			pq.push( a(tmp.start+(tmp.length+1) / 2,tmp.length/2 ) );
//			cout << tmp.start << ' ' << (tmp.length - 1) / 2 << "push" << endl;
//			cout << tmp.start + (tmp.length + 1) / 2 << ' ' << tmp.length / 2 << "push" << endl;
		}
		outFile << "Case #" << i << ": " << tmp.length / 2 << ' ' << (tmp.length - 1) / 2 << endl;

	}
	return 0;
}
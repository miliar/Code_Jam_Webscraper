#include <iostream>
#include <fstream>
#include <string>
#define ll long long
using namespace std;
#define MAX 1000

ifstream in("B-large.in");
ofstream out("output.txt");

int T, tt;
ll Num[MAX];



int main() {
	string Count;
	int prev;
	
	in >> T;
	for (tt = 1; tt <= T; ++tt) {
		out << "Case #" << tt << ": ";
		in >> Count;
		
		// 1자리인 경우 바로 출력
		if (Count.length() == 1) out << Count;
		else {
			int Len = Count.length();
			for (int i = 0; i < Len; ++i) Num[i] = int(Count.at(i)) - 48;
			
			// 완전수열인 경우
			int idx = 1;
			while (idx < Len && Num[idx] >= Num[idx - 1]) idx++;
			if (idx == Len) out << Count;

			// 완전 증가수열이 아닌 경우
			else {
				while (idx >= 1 && Num[idx] <= Num[idx - 1]) idx--;

				if (idx == 0) {
					if (Num[idx] == 1) {
						for(int i = 0; i < Len - 1; ++i) out << 9;
					}
					else {
						out << Num[idx] - 1;
						for (int i = 1; i < Len; ++i) out << 9;
					}
				}
				
				else {
					for (int i = 0; i < idx; ++i) out << Num[i];
					out << Num[idx] - 1;
					for (int i = idx + 1; i < Len; ++i) out << 9;
				}
			}
		}
			
		out << endl;
	}
	in.close();
	out.close();
}
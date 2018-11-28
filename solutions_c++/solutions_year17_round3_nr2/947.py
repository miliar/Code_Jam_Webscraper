// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cmath>

#define rep(i, a, b) for (int i=a;i<b;i++)
#define next(i) (i + 1) % 1440

using namespace std;


int main()
{
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	int T;
	reader >> T;
	int time[1440], ai[1440], bi[1440];
	rep(Ti, 0, T) {
		memset(time, 0, sizeof(time));
		int a, b, s, t;
		reader >> a >> b;
		int at = 720;
		int bt = 720;
		rep(i, 0, a) {
			reader >> s >> t;
			rep(j, s, t) time[j] = 2;
			bt -= (t - s);
		}
		rep(i, 0, b) {
			reader >> s >> t;
			rep(j, s, t) time[j] = 1;
			at -= (t - s);
		}
		int ans = 0;
		int as = 0;
		int bs = 0;
		int fnz = 0;
		while (fnz < 1440) {
			if (time[fnz] != 0 && time[next(fnz)] == 0) break;
			fnz++;
		}
		int k = fnz % 1440;
		cout << "fnz " << fnz << endl;
		int last, next, lastp;
		do {
			last = time[k];
			cout << k << endl; 
			lastp = k;
			if (time[next(k)] == 0) {
				while (time[next(k)] == 0) {
					k = next(k);
				}
				next = time[next(k)];
				if (next != last) ans++;
				else {
					if (next == 1) ai[as++] = (k + 1440 - lastp) % 1440;
					else bi[bs++] = (k + 1440 - lastp) % 1440;
				}
				k = next(k);
			}
			cout << "lastk " << k << endl;
			while (time[next(k)] != 0 && k != fnz) {
				if (time[next(k)] != time[k]) ans++;
				k = next(k);
				
			} 
			
		} while (k != fnz);
		sort(ai, ai + as);
		sort(bi, bi + bs);
		rep(i, 0, as) {
			cout << "aa" << i << ":" << ai[i] << endl;
			if (at >= ai[i]) at -= ai[i];
			else ans += 2;
		}
		rep(i, 0, bs) {
			if (bt >= bi[i]) bt -= bi[i];
			else ans += 2;
		}
		writer << "Case #" << Ti + 1 << ": " << ans << endl;
	}

	system("pause");
	return 0;
}


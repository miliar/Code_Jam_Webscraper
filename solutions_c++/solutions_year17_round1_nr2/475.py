#include <QCoreApplication>
#include <QString>
#include <QTextStream>
#include <QMap>
#include <QSet>
#include <QList>
#include <QString>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
using namespace std;


#if 1
void prework() {

}

int  cmp(int kit , int ind) {
	if (kit * 10 < ind * 9) return -1;
	if (kit * 10 > ind * 11) return 1;
	return 0;
}
void work(int order) {
	int n, p;
	cin >> n >> p;
	int ind[100];
	int zz[100];
	int w[100][100];
	for (int i = 0; i < n; i++) {
		cin >> ind[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			cin >> w[i][j];
		}
		std::sort(w[i], w[i] + p);
		zz[i] = 0;
	}


	int re = 0;

	int mul = 1;
	while (true) { 
		bool nowok = true;
		bool end = false;
		for (int i = 0; i < n; i++) {

			int need = ind[i] * mul;

			while (zz[i] < p && cmp(w[i][zz[i]], need) < 0) {
				zz[i] ++;
			}
			if (zz[i] == p) {
				end = true;
				break;
			}
			if (cmp(w[i][zz[i]], need) > 0) {
				nowok = false;
				break;
			}
		}
		if (end) break;
		if (nowok) {

			for (int i = 0; i < n; i++) {
				zz[i]++;
			}
			re++;
		}
		else {
			mul++;
		}
	}
	cout << re;
}

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	if (freopen("..\\temp\\output.txt", "w", stdout) == NULL)
		fprintf(stderr, "error redirecting stdout\n");
	if (freopen("..\\temp\\input.txt", "r", stdin) == NULL)
		fprintf(stderr, "error redirecting stdin\n");
	int t;
	cin >> t;
	prework();
	for (int i = 0; i<t; i++) {

		qDebug() << "case " << i + 1;
		cout << "Case #" << i + 1 << ": ";

		work(i + 1);
		cout << endl;
	}
	qDebug() << "end!";
	return 0;
	return a.exec();
}
#endif

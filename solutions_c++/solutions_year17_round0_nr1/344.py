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


void work(int order) {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int re = 0;
	for (int i = 0; i < s.size(); i++) {
		if (i + k > s.size()) break;
		if (s[i] == '+') continue;
		re++;
		for (int j = 0; j < k; j++) {
			int x = i + j;
			if (s[x] == '+') {
				s[x] = '-';
			}
			else {
				s[x] = '+';
			}
		}
	}

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
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

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
	qint64 n, k, n1,  f1,f2 ;
	cin >> n >> k;
	qint64 q1, q2, q3, q4;
	q1 = 1;
	q2 = 0;
	while (true) {
		q3 = 0;
		q4 = 0;
		auto x = n - 1; 
		
		if (x % 2 == 0) {
			f1 = f2 = x / 2;
			q3 += q1 * 2;
		}
		else {
			f1 = x / 2 + 1;
			f2 = x / 2;
			q3 += q1;
			q4 += q1;
		}
		n1 = f1;
		k -= q1;
		if (k <= 0) {
			cout << f1 << ' ' << f2;
			return  ;
		} 
			
		x = n - 2;
		if (x % 2 == 0) {
			f1 = f2 = x / 2;
			q4 += q2 * 2;
		}
		else {
			f1 = x / 2 + 1;
			f2 = x / 2;
			q3 += q2;
			q4 += q2;
		} 
		k -= q2;
		if (k <= 0) {
			cout << f1 << ' ' << f2;
			return;
		}

		n = n1;
		q1 = q3;
		q2 = q4;
	}

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

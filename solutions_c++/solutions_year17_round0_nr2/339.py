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
string check(string s) {
	if (s.size() == 1) {
		return s;
	}

	for (int i = 1; i < s.size(); i++) {
		if (s[i - 1] > s[i]) {
			auto f = stoll(s.substr(0,i));
			auto h = check(to_string(f - 1)); 
			h.append(s.size() - i, '9');
			return h;
		}
	}
	return s;
}

void work(int order) {
	string s;
	cin >> s;

	auto r =  check(s);
	for (int i = 0; i < r.size(); i++) {
		if (r[i] != '0') {
			cout << r.substr(i);
			return;
		}
	}
	int imp = 0;
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

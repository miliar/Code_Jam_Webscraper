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

#define fill0(x)  memset(x,0, sizeof(x));
bool ori1[110][110], ori2[110][110], re1[110][110], re2[110][110];
bool row[410], col[410], leftbot[410], rightbot[410];

void addver(int r, int c) {

	ori1[r][c] = true;
	leftbot[r + c] = true;
	rightbot[r - c + 100] = true;
}
void addhor(int r, int c) {

	ori2[r][c] = true;
	row[r] = true;
	col[c] = true;
}
void checkVer(int r, int c) {
	if (leftbot[r + c]) return;
	if (rightbot[r - c + 100]) return;
	re1[r][c] = true;
	leftbot[r + c] = true;
	rightbot[r - c + 100] = true;
}
void work(int order) {

	fill0(ori1);
	fill0(ori2);
	fill0(re1);
	fill0(re2);
	fill0(row);
	fill0(col);
	fill0(leftbot);
	fill0(rightbot);

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		char x;
		cin >> x;
		int r, c;
		cin >> r >> c; 
		if (x == 'x') {
			addhor(r-1, c-1);
		}
		else if (x == '+') {
			addver(r-1, c-1);
		}
		else if (x == 'o') {
			addhor(r-1, c-1);
			addver(r-1, c-1);
		}
	}

	for (int i = 0; i < n; i++) {
		if (row[i] == true) continue;
		for (int j = 0; j < n; j++) {
			if (col[j] == false) {
				re2[i][j] = true;
				row[i] = true;
				col[j] = true;
				break;
			}
		}
	} 

	int dis;
	if (n % 2 == 0) {
		dis = n / 2;
	}
	else {
		dis = n / 2 + 1;
	}
	for (int x = 0; x < dis; x++) {
		for (int i = 0; i < n; i++) {
			checkVer(x, i);
			checkVer(n - 1 - x, i);
			checkVer(i, x);
			checkVer(i, n - 1-x);
		}
	}

	int count = 0;
	int add = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (ori1[i][j]) count++;
			if (ori2[i][j]) count++;
			if (re1[i][j]) count++;
			if (re2[i][j]) count++;

			if (re1[i][j] || re2[i][j]) add++;
		}
	}

	cout << count << ' ' << add;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (re1[i][j] || re2[i][j]) {}
			else continue;

			bool all = (ori1[i][j] || re1[i][j]) && (re2[i][j] || ori2[i][j]);
			if (all) {
				cout <<endl << "o " << i + 1 << ' ' << j + 1;
				continue;
			}
			if (re1[i][j]) {
				cout << endl << "+ " << i + 1 << ' ' << j + 1;
				continue;
			}			
			if (re2[i][j]) {
				cout << endl << "x " << i + 1 << ' ' << j + 1;
				continue;
			}
			assert(false);
		}
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

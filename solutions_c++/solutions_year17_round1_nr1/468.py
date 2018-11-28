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
	char grid[100][100];
	int r, c;
	cin >> r >> c;

	for (int i = 0; i < r; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < c; j++) {
			grid[i][j] = s[j];
		}
	}
	int lastLine = 100;
	for (int i = 0; i < r; i++) {
		char now = '?';
		for (int j = 0; j < c; j++) {
			if (grid[i][j] == '?')  continue;
			now = grid[i][j];
			int z = j - 1;
			while (z>=0 && grid[i][z] == '?') {
				grid[i][z] = now;
				z--;
			}
		}
		if (now == '?') continue;
		lastLine = i;
		int z = c - 1;
		while (z >= 0 && grid[i][z] == '?') {
			grid[i][z] = now;
			z--;
		}

		int x = i - 1;
		while (x >= 0 && grid[x][0] == '?') {
			memcpy(grid[x], grid[i], 100);
			x--;
		}
	}
	int x = lastLine + 1;
	while ( x < r) {
		memcpy(grid[x], grid[lastLine], 100);
		x++;
	}
	for (int i = 0; i < r; i++) {
		cout << endl;
		for (int j = 0; j < c; j++) {
			cout << grid[i][j];
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

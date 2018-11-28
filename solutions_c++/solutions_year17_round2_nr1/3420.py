#include <iostream>
#include <string>
#include <fstream>>
#include <iomanip>
using namespace std;

int n;
ifstream fin("input.txt");
ofstream fout("output.txt");
int cnt;

int x, y;
double long speed, res;
int k, s;
void input() {


	fin >> x >> y;
	speed = 0;


	for (int i = 0; i < y; i++) 
	{
		fin >> k >> s;

		if (speed < double(x - k) / s) {
			speed = double(x - k) / s;
		}
	}

}

void proc() {
	res = 0.000000;
	res = double(x / speed);

}

void output(int k) {
	k++;

		fout << "Case #";
		fout << k;
		fout << ": ";
		fout << fixed;
		fout.precision(6);
		fout << setiosflags(ios::showpoint) << res;
		fout << endl;
}
void main()
{

	fin >> n;
	for (int i = 0; i < n; i++) {
		input();

		proc();
		output(i);
	}


}
#include <vector>
#include <string>
#include <iostream>
#include <map>

using namespace std;

bool barrera(string &str, char le, int K, int W) {
	for (int i = 0; i < str.size(); i++)
	{
		if (i + K > str.size())
			break;

		//if (i>=W && i<=W + K)
		//	continue;
		bool ig = true;
		for (size_t j = i; j < i+K && j < str.size(); j++)
		{

			if (str[j] != le) {
				ig = false;
				break;
			}
		}
		if (ig)
			return true;
	}

	return false;
}

bool sonIguales(string &str, char le, int pos, int K) {
	for (int i = pos; i < pos+K && i < str.size(); i++)
	{
		if (str[i] != le) {
			return false;
		}
	}

	return true;
}
void panStats(string &str, int pos, int K, int &po, int &ne) {
	for (int i = pos; i < pos + K && i < str.size(); i++)
	{
		if (str[i] == '+') {
			++po;
		}
		else {
			++ne;
		}
	}

}
void flipStats(string &str, int pos, int K, int &po, int &ne) {
	for (int i = pos; i < pos + K && i < str.size(); i++)
	{
		if (str[i] == '+') {
			++ne;
		}
		else {
			++po;
		}
	}

}
bool libre(int pos, int K, vector<bool> &mark) {
	//if (pos + K > mark.size()) {
	//	return false;
	//}
	for (size_t i = pos; i < pos+K && i < mark.size(); i++)
	{
		if (mark[i]) {
			return false;
		}
	}
	return true;
}
void flip(string &str, int pos, int K) {
	for (int i = pos; i < pos + K && i < str.size(); i++)
	{
		if (str[i] == '+') {
			str[i] = '-';
		}
		else {
			str[i] = '+';
		}
	}

}

int mini;
void BT(int pos, string &str, int K, int localmini, int posi, int nega, vector<bool> &mark, map<string, bool> mmap) {
	for (int i =0; i < str.size(); i++)
	{
		//if (i+K <= str.size() && libre(i, K, mark)) {
		if (i + K <= str.size() && !mark[i]) {
		//if (i + K <= str.size()) {
			int po = 0, ne = 0;
			flipStats(str, i, K, po, ne);
			
			if (ne == K)continue;

			int absPo = posi + po-ne;
			int absNeg = nega+ ne-po;
			/*
			if (absNeg > absPo) {
				continue;
			}*/

			/*if (posi+po - ne-nega <0)
				continue;*/
			
			string cop = str;
			flip(str, i, K);

			map<string, bool>::iterator it = mmap.find(str);
			if (it != mmap.end() && it->second) {
				continue;
			}
			mmap[str] = true;
			
			if (ne > po && !barrera(str, '-', K, i)) {

				mmap[str] = false;
				str = cop;
				continue;
			}

			//for (size_t j = 0; j < K; j++) mark[i + j] = true;
			mark[i] = true;
			if (sonIguales(str, '+', 0, str.size())) {
				if (localmini+1 < mini) {
					mini = localmini+1;
				}
			}
			else {
				BT(i + K, str, K, localmini + 1, absPo, absNeg, mark, mmap);
			}
			mark[i] = false;

			mmap[str] = false;
			str = cop;
		}
	}
}

int main() {
	//freopen("entrada.in", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	//
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		string pans;
		int K;
		cin >> pans >> K;

		int cant = 0x3f3f3f3f;
		if (sonIguales(pans, '+', 0, pans.size())) {
			cant = 0;
		}
		else {
			mini = 0x3f3f3f3f;
			int po=0, ne = 0;
			vector<bool> mark(pans.size(), false);
			panStats(pans, 0, pans.size(), po, ne);
			map<string, bool> mmap;
			BT(0, pans, K, 0, po, ne, mark, mmap);
			cant = mini;
		}
		cout << "Case #" << i+1 << ": ";
		if (cant == 0x3f3f3f3f)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cant << endl;
	}
	return 0;
}
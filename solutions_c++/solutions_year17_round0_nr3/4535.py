#include<iostream>
#include<deque>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream inFile;
	ofstream outFile;
	inFile.open("C-large.in");
	outFile.open("c.out");
	long long int stall, man, num = 0, sum;
	long long int	jishu, oushu;
	long long int  jishu_size = 0, oushu_size = 0;
	inFile >> sum;
	for (long long int i = 1;i <= sum;++i)
	{
		inFile >> stall >> man;
		jishu=oushu=0,jishu_size = oushu_size = 0;
		if (stall % 2)  jishu = stall, ++jishu_size;
		else oushu = stall, ++oushu_size;
		if (man >= stall)
		{
			outFile << "Case #" << i << ": " << 0 << " " << 0 << endl;
			jishu_size = 0, oushu_size = 0;continue;
		}
		while (2) {
		   if (jishu == 0) jishu_size = 0;
			if (oushu == 0) oushu_size = 0;
			long long int x = jishu_size, y = oushu_size;
			if (jishu_size&&oushu_size) {
				long long int jishu_z = (jishu - 1) / 2;
				long long int daoushu = oushu  / 2;
				long long int xiaooushu = oushu - daoushu-1;
				if (jishu > oushu) {
					man -= jishu_size;
					if (man <= 0) {
						outFile << "Case #" << i << ": " << jishu_z << " " << jishu_z << endl;
						break;}
					man -= oushu_size;
					if (man <= 0) {
						outFile << "Case #" << i << ": " << daoushu << " " << xiaooushu << endl;
						break;}
				}
				else if (oushu >= jishu) {
					man -= oushu_size;
					if (man <= 0) {
						outFile << "Case #" << i << ": " << daoushu << " " << xiaooushu << endl;
						break;}
					man -= jishu_size;
					if (man <= 0) {
						outFile << "Case #" << i << ": " << jishu_z << " " << jishu_z << endl;
						break;}
				}
				jishu_size = oushu_size = y;
				if (jishu_z % 2) { jishu_size += x * 2; }
				else { oushu_size += x * 2; }
				if (xiaooushu % 2) { jishu = xiaooushu, oushu = daoushu; }
				else { jishu = daoushu, oushu = xiaooushu; }
			}
			else if (jishu_size == 0 && oushu_size) {
				long long int daoushu = oushu  / 2;
				long long int xiaooushu = oushu - daoushu-1;
				man -= oushu_size;
				if (man <= 0){
					outFile << "Case #" << i << ": " << daoushu << " " << xiaooushu << endl;
					break;}
				jishu_size = oushu_size = y;
				if (daoushu % 2) { jishu = daoushu;oushu=xiaooushu; }
				else { jishu = xiaooushu, oushu = daoushu; }
			}
			else if (oushu_size == 0 && jishu_size) {
				long long int jishu_z = (jishu - 1) / 2;
				man -= jishu_size;
				if (man <= 0) {
					outFile << "Case #" << i << ": " << jishu_z << " " << jishu_z << endl;
					break;}
				if (jishu_z % 2) jishu = jishu_z, jishu_size=jishu_size* 2;
				else { oushu = jishu_z, oushu_size = jishu_size * 2, jishu_size = 0; }
			}
			if (jishu == 0) jishu_size = 0;
			if (oushu == 0) oushu_size = 0;
		}
	}
}

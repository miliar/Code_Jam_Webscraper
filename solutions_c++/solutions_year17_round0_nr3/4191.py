#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
	argv[1] = "D:\\Other\\BISHI\\GoogleCodeJam\\C\\C-small-1-attempt0.in";
	argv[2] = "D:\\Other\\BISHI\\GoogleCodeJam\\C\\C-small-1-attempt0.out";

	//ifstream fin(stdin);
	//ofstream fout(stdout);
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	string line;
	getline(fin, line);
	int testNum = stoi(line);
	for (int i = 0; i < testNum; i++)
	{
		getline(fin, line);
		int space = line.find(" ");
		int N = stoi(line.substr(0, space));
		int K = stoi(line.substr(space + 1, line.length() - space - 1));
		
		queue<int> que;
		que.push(N);
		int max = 0, min = 0;
		for (int i = 0; i < K; )
		{
			int repeatNum = 0;
			int cur = que.front();//取一个数出来
			que.pop();
			repeatNum++;
			while (!que.empty() && que.front() == cur)//把同样大小的数都取出来
			{
				que.pop();
				repeatNum++;
			}

			if (cur % 2 == 0)//偶数时对应分解成的左右两个数
			{
				max = cur / 2;
				min = (cur - 1) / 2;
			}
			else//奇数
			{
				max = cur / 2;
				min = max;
			}

			i += repeatNum;//每提一个数出来都是一次选座
			if (i >= K)//想求的第K次选座包含在本次处理中
				break;
			for (int j = 0; j < repeatNum; j++)//还没到第K次则把此次分出来的数字按大小顺序装进队列
				que.push(max);
			for (int j = 0; j < repeatNum; j++)
				que.push(min);
		}
		
		fout << "Case #" << i + 1 << ": " << max << " " << min << endl;
	}

	fin.close();
	fout.close();
}
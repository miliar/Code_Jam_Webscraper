#include<iostream>
#include<string>
#include<map>
#include<queue>
using namespace std;
struct Node
{
	string value;
	int count;
};
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Case = 1; Case <= T; Case++)
	{
		map<string, int> check;
		queue<Node> q;
		string input;
		int k;
		cin >> input >> k;
		check[input] = 1;
		printf("Case #%d: ", Case);
		Node node = { input, 0 };
		q.push(node);
		bool flag = false;
		while (q.empty() == false)
		{
			node = q.front();
			q.pop();
			int i;
			for (i = 0; i < node.value.length(); i++)
			{
				if (node.value[i] == '-')
					break;
			}
			if (i == node.value.length())
			{
				flag = true;
				printf("%d\n", node.count);
				break;
			}
			for (i = 0; i < node.value.length() - k + 1; i++)
			{
				string temp = node.value;
				for (int j = 0; j < k; j++)
				{
					if (temp[i + j] == '+') temp[i + j] = '-';
					else temp[i + j] = '+';
				}
				if (check.count(temp) <= 0)
				{
					check[temp] = 1;
					Node tempNode = { temp, node.count + 1 };
					q.push(tempNode);
				}
			}
		}
		if (!flag)
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
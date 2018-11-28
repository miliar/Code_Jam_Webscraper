void solver(string& s,int index)
{
	int n = s.size();
	if (index==(n-1))return;
	if (s[index] > s[index + 1])
	{
		s[index] -= 1;
		for (int i = index + 1; i < n; i++)s[i] = '9';
		if(index>=1)
			solver(s, index - 1);
	}
	else solver(s, index + 1);
}
int main()
{
	freopen("d:/codejam/B-small-attempt0.in", "r", stdin);
	freopen("d:/codejam/BSmall.out", "w", stdout);
	int T;
	cin >> T;
	long long int num;
	for (int i = 1; i <= T; i++)
	{
		cin >> num;
		if (num < 10)
		{
			printf("Case #%d: %lld\n", i, num);
			continue;
		}
		stringstream ss;
		string s_num;
		ss << num;
		ss >> s_num;
		solver(s_num, 0);
		ss.clear();
		ss << s_num;
		ss >> num;
		printf("Case #%d: %lld\n", i, num);
	}
}
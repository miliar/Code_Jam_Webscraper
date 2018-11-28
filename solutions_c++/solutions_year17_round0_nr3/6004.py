#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

void print_table(multiset<int> table, multiset<int>::iterator it)
{
	for(it = table.begin();it != table.end();it++)
		printf("%d ", *it);
	printf("\n");
}

int main()
{
	int t, caseNum = 1, i, j, n, k, max, min, now;
	multiset<int> table;
	multiset<int>::iterator it;
	scanf("%d", &t);
	while(t--){
		scanf("%d%d", &n, &k);
		table.clear();
		table.insert(n);
		while(k--){
			it = table.end();
			it--;
			now = *it;
			table.erase(it);
			if(now % 2 == 0){
				max = now / 2;
				min = max - 1;
			}else{
				max = min = (now - 1) / 2;
			}
			table.insert(max);
			table.insert(min);
		}
		printf("Case #%d: %d %d\n", caseNum++, max, min);
	}
	return 0;
}

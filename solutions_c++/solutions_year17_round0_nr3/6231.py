#include <stdio.h>


typedef struct {
	int leftSize, rightSize;
	int leftIndex, rightIndex;
} NODE;

NODE nodes[1000010];
int count;

int recur(int index, int size) {
	if(index == -1 || index >= count) {
		nodes[count].leftIndex = -1;
		nodes[count].rightIndex = -1;
		nodes[count].leftSize = size/2;
		nodes[count].rightSize = size/2;
		if(size%2 == 0)
			nodes[count].leftSize--;
		count++;
		return 1;
	}

	if(nodes[index].leftSize < nodes[index].rightSize) {
		if(recur(nodes[index].rightIndex, nodes[index].rightSize--)) {
			nodes[index].rightIndex = count-1;
		}
	}
	else {
		if(recur(nodes[index].leftIndex, nodes[index].leftSize--)) {
			nodes[index].leftIndex = count-1;
		}
	}

	return 0;
}

int main() {
	int T;
	scanf("%d", &T);

	for(int i = 1; i <= T; i++) {
		int n, k;
		scanf("%d %d", &n, &k);

		count = 0;

		for(int j = 0; j < k; j++) {
			recur(0, n);
		}

		int max = nodes[count-1].leftSize, min = nodes[count-1].rightSize;
		if(nodes[count-1].leftSize < nodes[count-1].rightSize) {
			max = nodes[count-1].rightSize;
			min = nodes[count-1].leftSize;
		}

		printf("Case #%d: %d %d\n", i, max, min);
	}

	return 0;
}
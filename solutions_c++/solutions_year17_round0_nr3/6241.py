//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by nastia on 08/04/2017.
//  Copyright © 2017 Anastasiia Soboleva. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;
//BATHROOM STALLS

typedef struct node {
	
	unsigned long long availablePositions;
	unsigned long long maximum;
	struct node *leftNode;
	struct node *rightNode;
	
} node;

node empty_node = {
	0,
	0,
	nullptr,
	nullptr
};

unsigned long long half(unsigned long long n) {
	return (unsigned long long)round((double)n/2);
}

void update_maximum(node *head) {
	
	if (head->availablePositions == head->maximum) {
		//no children, we should create them
		unsigned long long n = head->availablePositions;
		unsigned long long h = half(n);
		unsigned long long leftHalf = h - 1;
		unsigned long long rightHalf = n - h;
		
		head->leftNode = (node *)malloc(sizeof(node));
		head->leftNode->leftNode = nullptr;
		head->leftNode->rightNode = nullptr;
		head->leftNode->availablePositions = leftHalf;
		head->leftNode->maximum = leftHalf;
		
		head->rightNode = (node *)malloc(sizeof(node));
		head->rightNode->rightNode = nullptr;
		head->rightNode->leftNode = nullptr;
		head->rightNode->availablePositions = rightHalf;
		head->rightNode->maximum = rightHalf;
		
		head->maximum = max(leftHalf, rightHalf);
		
	} else {
		
		if (head->leftNode->maximum >= head->rightNode->maximum) {
			update_maximum(head->leftNode);
		} else {
			update_maximum(head->rightNode);
		}
		head->maximum = head->leftNode->maximum >= head->rightNode->maximum ? head->leftNode->maximum : head->rightNode->maximum;
	}
}

void findPosition(unsigned long long n, unsigned long long k, ofstream& file, int case_num) {
	
	node *tree = &empty_node;
	tree->availablePositions = n;
	tree->maximum = n;
	
	for (int i = 1; i < k; i++) {
		update_maximum(tree);
	}
	
	//RESULT
	unsigned long long res = tree->maximum;
	unsigned long long h = half(res);
	unsigned long long leftResult = h - 1;
	unsigned long long rightResult = res - h;
	unsigned long long maximum_value = max(leftResult, rightResult);
	unsigned long long minimum_value = min(leftResult, rightResult);
	file << "Case #" << case_num << ": " << maximum_value << " " << minimum_value << endl;
}

int main(int argc, const char * argv[]) {
	ifstream myfile;
	ofstream outputFile;
	
	outputFile.open("/Users/nastia/Developer/GoogleCodeJam2017/res.out",std::ios_base::in);
	myfile.open("/Users/nastia/Downloads/C-small-2-attempt0.in.txt");
	
	int t;
	myfile >> t;
	for (int j = 1; j <= t; j++) {
		unsigned long long n, k;
		myfile >> n >> k;
		findPosition(n, k, outputFile, j);
	}
	myfile.close();
	return 0;
}

#include <stdio.h>
void merge(int* array, int* tmp, size_t left, size_t right){
    size_t middleIndex = (left+right)/2;
    size_t leftIndex = left;
    size_t rightIndex = middleIndex+1;
    size_t tmpIndex = left;

    while(leftIndex <= middleIndex && rightIndex <= right){
        if(array[leftIndex] <= array[rightIndex]){
            tmp[tmpIndex]=array[leftIndex++];
        }else{
            tmp[tmpIndex]= array[rightIndex++];
        }
        tmpIndex++;
    }
    while(leftIndex <= middleIndex){
        tmp[tmpIndex++]= array[leftIndex++];
    }
    while(rightIndex <=right){
        tmp[tmpIndex++]=array[rightIndex++];
    }
}

void mergeSort(int* array,int* tmp, size_t left, size_t right){
    if(left == right) return;
    size_t middleIndex=(left+right)/2;
    mergeSort(array, tmp, left, middleIndex);
    mergeSort(array,tmp,middleIndex+1,right);
    merge(array,tmp,left, right);
    for(size_t i=left; i<=right;i++){
        array[i]=tmp[i];
    }
}

void printArray(int* array, int c){
    for(int i=0; i< c;i++){
        printf("%d, ",array[i]);
    }
    printf("\n");
}
int main() {
    int array1[10]={1,2,4,8,2,5,10,5,11,3};
    int tmp[10];
    mergeSort(array1, tmp, 0,9);
    printArray(array1,10);

}
